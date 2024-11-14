# Tobias Senti <git@tsenti.li>

### Tries to find all connections for a given block -> checks if they exist or not

import utils
from xcxk import devices

# For IOBs the blk_name is PADXX
def find_local_long_pips_for_block(dev, package, speed, blk_name, pin, unique = False):
    local_wires = devices.get_dev_local_wires(dev)
    long_wires = devices.get_dev_long_wires(dev)
    rows = devices.get_device_rows(dev)
    cols = devices.get_device_cols(dev)

    pip_names = []
    for local in local_wires:
        for col in cols:
            pip_names.append(f'col.{col}.local.{local}:{blk_name}.{pin}')
        for row in rows:
            pip_names.append(f'row.{row}.local.{local}:{blk_name}.{pin}')
    for long in long_wires:
        for col in cols:
            pip_names.append(f'col.{col}.long.{long}:{blk_name}.{pin}')
        for row in rows:
            pip_names.append(f'row.{row}.long.{long}:{blk_name}.{pin}')
    
    lca = ''
    for name in pip_names:
        lca += f'NProgram {name}\n'
    lca += '\n'

    filename = f'{blk_name}_{pin}'
    filename = utils.create_lca(filename, dev, package, speed, lca, unique)
    log = utils.create_bit(filename)

    existing_pips = []
    for name in pip_names:
        if name not in log:
            print(f'Pip {name} exists')
            existing_pips.append(name)

    return (existing_pips, log)

