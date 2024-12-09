#!/bin/env python3
from struct import unpack
from sys import argv
from os import chmod

def u16(buf: bytes) -> int:
    return unpack('<H', buf)[0]

def u32(buf: bytes) -> int:
    return unpack('<I', buf)[0]

try:
    infile  = argv[1]
    outfile = argv[2]
except IndexError as e:
    print('Require infile and outfile.')
    exit(1)

with open(infile, 'rb') as inf:
    buffer = inf.read(0x1000)

    ehsize = u16(buffer[0x34:0x36])
    phsize = u16(buffer[0x36:0x38])
    phnum  = u16(buffer[0x38:0x3a])

    cursor = ehsize
    rxbyte = None
    for i in range(phnum):
        # ptype == PT::LOAD and pflags == R | X
        if u32(buffer[cursor:cursor + 4]) == 1 and u16(buffer[cursor + 4:cursor + 6]) == 5:
            rxbyte = cursor + 4
            break
        cursor += phsize

    if rxbyte is None:
        print('Section .text not found!')
        exit(1)

    with open(outfile, 'wb') as outf:
        outf.write(buffer[:rxbyte] + b'\x07' + buffer[rxbyte + 1:])
        outf.write(inf.read())

    chmod(outfile, 0o755)
