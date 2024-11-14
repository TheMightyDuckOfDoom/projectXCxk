from xcxk import parser
from xcxk import container

def bit2bits(fin, fout, format='BIT'):
    bit2bitsf(open(fin, 'r'), open(fout, 'w'))

def bit2bitsf(fin, fout, format='BIT'):
    p = parser.Parser(container.getbits(fin, format))

    for framei, frame in enumerate(p.frames()):
        for biti, bit in enumerate(frame['payload']):
            if bit:
                fout.write('bit_%02x_%02x\n' % (framei, biti))
