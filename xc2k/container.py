# Copyright (C) 2018  John McMaster <JohnDMcMaster@gmail.com>
# https://github.com/JohnDMcMaster/project2064
  
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
  
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import bitstring

def revbits8(n):
    return int('{:08b}'.format(n)[::-1], 2)

def revbits4(n):
    return int('{:04b}'.format(n)[::-1], 2)

def revnib(n):
    return ((n & 0xF) << 4) | ((n >> 4) & 0xF)

def munge(n):
    return (revbits4(n & 0xF) << 4) | revbits4((n >> 4) & 0xF)

def getbits_bin(f):
    return bitstring.ConstBitStream(bytes=f.read())

def getbits_bit(f):
    # .BIT w/ header
    buff = f.read()
    buff = buff[0x76:]
    return bitstring.ConstBitStream(bytes=buff)

def getbits_rom(f):
    # random rom file they gave me
    buff = bytearray()
    for b in f.read():
        # Reverse bits, swap nibbles
        buff += chr(munge(ord(b)))
    return bitstring.ConstBitStream(bytes=buff)

def getbits(f, format='BIT'):
    bits = {
        'bin': getbits_bin,
        'BIT': getbits_bit,
        'rom': getbits_rom,
        }[format](f)
    return bits