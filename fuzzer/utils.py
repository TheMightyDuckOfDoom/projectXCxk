# Tobias Senti <git@tsenti.li>

from xc2k import xact

def create_lca(filename, device, package, speed, lca_content):
    with open(filename, 'w') as f:
        f.write('Version 2\n')
        f.write(f'Design {device}{package}\n')
        f.write(f'Speed {speed}\n\n')
        f.write(lca_content)

def create_bit(filename):
    log = xact.lca2bit("./designs", filename)
    print(log)