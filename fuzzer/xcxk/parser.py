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

'''
Figure 13. XC2064 Internal Configuration Data Arrangement
11111111                DUMMY BITS (4 BITS MINIMUM) XACT 2.10 GENERATE 8 BITS
0010                    PREAMBLE CODE
<24-BIT LENGTH COUNT>   CONFIGURATION PROGRAM LENGTH
1111                    DUMMY BITS (4 BITS MINIMUM)
0 <DATA FRAME # 0001> 111
0 <DATA FRAME # 0002> 111
0 <DATA FRAME # 0003> 111
...
1111                    POSTAMBLE CODE (4 BITS MIMIMUM)


DATA PROGRAM DATA
REPEATED FOR EACH LOGIC CELL ARRAY IN DAISY CHAIN
                        XC2018        XC2064
CONFIGURATION FRAMES    196            160
BITS PER FRAME    87            71

START-UP REQUIRES THREE CONFIGURATION CLOCKS BEYOND LENGTH COUNT
'''

from . import devices

class Parser(object):
    def __init__(self, bits, dev):
        if not devices.is_device_valid(dev):
            raise Exception('Invalid device %s' % dev)
        self.dev = dev
        self.nframes = devices.get_dev_num_frames(dev)
        self.frame_bits = devices.get_dev_frame_bits(dev)
        self.bits = bits
        self.cfglen = None

    def expect(self, want, nbits, msg='expect'):
        got = self.bits.read(nbits).uint
        if want != got:
            raise Exception('%s: want 0x%x, got 0x%x' % (msg, want, got))
        return got

    def expect_run(self, want, minrun, msg):
        '''Keep grabbing bits of type want until not want comes'''
        ret = ''
        while self.bits.pos < len(self.bits):
            p = self.bits.peek(1).uint
            if p != want:
                break
            ret += str(self.bits.read(1).uint)
        if len(ret) < minrun:
            raise Exception("%s: want at least %d bits, got %d" % (msg, want, len(ret)))
        return ret

    def header(self):
        # 4 min, but 8 is typical value (at least XACT 2.10 does)
        pad1 = self.expect_run(1, 4, 'dummy bits 1')
        preamble = self.expect(0b0010, 4, 'preamble code')
        self.cfglen = self.bits.read(24).uint
        pad2 = self.expect_run(1, 4, 'dummy bits 2')
        return {'pad1': pad1, 'preamble': preamble, 'length': self.cfglen, 'pad2': pad2}

    def frame(self):
        preamble = self.expect(0b0, 1, 'frame preamble')
        payload = self.bits.read(self.frame_bits)
        postamble = self.expect(0b111, 3, 'frame postamble')
        return {'preamble': preamble, 'payload': payload, 'postamble': postamble}

    def frames_raw(self):
        ret = []
        for _framei in range(self.nframes):
            ret.append(self.frame())
        return ret

    def frames(self):
        self.header()
        ret = self.frames_raw()
        self.footer()
        return ret

    def footer(self):
        postamble = self.expect_run(1, 4, 'postamble')
        return {'postamble': postamble}
