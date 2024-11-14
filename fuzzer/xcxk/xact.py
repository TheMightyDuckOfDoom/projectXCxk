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
XACT=/opt/XACT

echo >RUN.BAT
echo "D:" >>RUN.BAT
echo "CD D:\DATA" >>RUN.BAT
echo "D:\MAKEBITS -V -O C:\DESIGN.BIT C:\DESIGN.LCA" >>RUN.BAT

SDL_VIDEODRIVER=dummy dosbox RUN.BAT -c "MOUNT D: $XACT" -exit
'''

import os
import subprocess

XACT_DIR = os.getenv('XACT_DIR', './XACT')

def lca2bit(lca_dir, design_name):
    '''
    Take LCA text file named {design_name}.LCA in lca_dir and compile to BIT file in same directory
    ''' 
    name = design_name[:7]
    batch = f'''\
D:
CD D:\DATA
D:\MAKEBITS -V -O C:\{design_name}.BIT C:\{design_name}.LCA > C:\{name}.LOG
'''
    batch_name = name + '.BAT'
    batch_fn = os.path.join(lca_dir, batch_name)
    try:
        open(batch_fn, 'w').write(batch)
        result = subprocess.check_output('SDL_VIDEODRIVER=dummy dosbox %s -c "MOUNT D: %s" -exit >/dev/null' % (batch_fn, XACT_DIR), shell=True, text=True)
        print(result)
    finally:
        if os.path.exists(batch_fn):
            os.unlink(batch_fn)
        with open(os.path.join(lca_dir, f'{name}.LOG')) as f:
            log = f.read()
            return log
