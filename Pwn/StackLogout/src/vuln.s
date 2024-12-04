	.file	"who.s"
	.intel_syntax noprefix
	.text
	.section	.rodata.str1.8,"aMS",@progbits,1
	.align 8
.sWarningNonAscii:
	.string	"The input contains non-ascii chars!"
	.align 8
.sNeedCast:
	.string	"It is needed to be converted to ISO-2022-CN-EXT."
	.section	.rodata.str1.1,"aMS",@progbits,1
.sFromEnc:
	.string	"UTF-8"
.sToEnc:
	.string	"ISO-2022-CN-EXT"
.sConfirm:
	.string	"Do you confirm? [y/n] "
	.text
	.p2align 4
	.globl	who
	.type	who, @function
who:
    # init stack frame
	push	rbp
	mov	rbp, rsp
    sub rsp, 0x10
    # canary & toread init
.equ canary, 8
.equ toread, 0x10
    mov rax, QWORD PTR fs:[0x28]
    mov QWORD PTR [rbp - canary], rax
	mov	eax, esi
    # alloca(size): local, tmp
    sub rsp, rax
    sub rsp, rax
    dec eax
    # toread = size - 1
    mov DWORD PTR [rbp - toread], eax

    # now we'll calc rest of vars according to rsp
    # alloca: pbuf, inval, outval
    sub rsp, 0x20
    # save registers
    push rdi
    push rbx
    push r12
    push r13
    push r14
    push r15
    # r14 = size
    mov r14d, esi
    # xmm0 = 0
    pxor xmm0, xmm0
.equ tmp, 0x50
.equ buf, 0x28
.equ inval, 0x38
.equ outval, 0x40
.equ pbuf, 0x48
.equ ptmp, 0x30
    # r13 = local
    lea r13, QWORD PTR [rsp + r14 * 1 + tmp]
    # pbuf = local, ptmp = tmp
    mov QWORD PTR [rsp + pbuf], r13
    lea r9, QWORD PTR [rsp + tmp]
    mov QWORD PTR [rsp + ptmp], r9
    # memset(local, 0, size)
    mov rbx, r13
    mov rcx, r14
    add rcx, rbx            # rcx = local + size
.setmem:                    # rcx != rbx
    movaps XMMWORD PTR [rbx], xmm0
    add rbx, 0x10
    cmp rbx, rcx
    jb .setmem
    
    # r12 = readin = read(0, local, toread)
    mov edx, DWORD PTR [rbp - toread]
    mov rsi, r13
    xor edi, edi
    call read@PLT
    mov r12, rax
    # inval = outval = readin
    mov QWORD PTR [rsp + inval], rax
    mov QWORD PTR [rsp + outval], rax
    
    # xmm1 (mask) = 0x80 * 16
	mov	edx, 0x80808080
	movd	xmm1, edx
	pshufd	xmm1, xmm1, 0
    # rdi = local, rsi = local + size
    mov rdi, r13
    mov rsi, r14
    add rsi, rdi

    # local includes non-ascii byte?
.testbit:                   # rsi != rdi
    movdqa xmm2, XMMWORD PTR [rdi]
    pand xmm2, xmm1
    pmovmskb eax, xmm2
    test eax, eax
    jne .convert
    add rdi, 0x10
    cmp rdi, rsi
    jb .testbit
.testname:
    # printf("Do you confirm? [y/n] ")
    lea rdi, QWORD PTR [rip + .sConfirm]
    xor eax, eax
    call printf@PLT
    # c = getchar()
    mov rdi, QWORD PTR [rip + stdin]
    call getc@PLT
    mov r15d, eax
    # getchar() // discard '\n'
    mov rdi, QWORD PTR [rip + stdin]
    call getc@PLT
    # c ?= 'n'
    cmp r15d, 0x6e
    je .oneMoreRead
    # c ?= 'y'
    cmp r15d, 0x79
    jne .testname
.goback:
    # memcpy(buf, local, readin)
    mov rdx, r12
    mov rsi, r13
    mov rdi, QWORD PTR [rsp + buf]
    call memcpy@PLT
    
    # test canary
    mov rax, QWORD PTR [rbp - canary]
    mov rcx, QWORD PTR fs:[0x28]
    cmp rax, rcx
    jne .stack_chk_failed

    # restore registers
    pop r15
    pop r14
    pop r13
    pop r12
    pop rbx
    leave
    ret

.oneMoreRead:
    # r12 = readin = read(0, local, toread & 0x1f0)
    mov edx, DWORD PTR [rbp - toread]
    and edx, 0x1f0
    mov rsi, r13
    xor edi, edi
    call read@PLT
    mov r12, rax
    jmp .goback


.convert:
    # memcpy(tmp, local, size)
    mov rdx, r14
    mov rsi, r13
    lea rdi, QWORD PTR [rsp + tmp]
    call memcpy@PLT
    # puts("The input contains non-ascii chars!")
    lea rdi, QWORD PTR [rip + .sWarningNonAscii]
    call puts@PLT
    # puts("It is needed to be converted to ISO-2022-CN-EXT.")
    lea rdi, QWORD PTR [rip + .sNeedCast]
    call puts@PLT
    # cd = iconv_open("ISO-2022-CN-EXT", "UTF-8")
    lea rsi, QWORD PTR [rip + .sFromEnc]
    lea rdi, QWORD PTR [rip + .sToEnc]
    call iconv_open@PLT
    mov r15, rax
    # iconv(cd, &ptmp, &inval, &pbuf, &outval)
    lea r8,  QWORD PTR [rsp + outval]
    lea rcx, QWORD PTR [rsp + pbuf]
    lea rdx, QWORD PTR [rsp + inval]
    lea rsi, QWORD PTR [rsp + ptmp]
    mov rdi, rax
    call iconv@PLT
    # iconv_close(cd)
    mov rdi, r15
    call iconv_close@PLT
    jmp .testname

.stack_chk_failed:
    call __stack_chk_fail@PLT
    # no return

.LFE6577:
	.size	who, .-who
	.ident	"Rocket: (Arch Linux) 20241205"
	.section	.note.GNU-stack,"",@progbits
