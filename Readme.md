# ProjectXCxk: Reverse-engineering of early Xilinx FPGAs

This project is based on [JohnDMcMaster/project2064](https://github.com/JohnDMcMaster/project2064).

The current target is the XC3000.

Both the XC3000A and XC3000L have additional routing resources.
Getting the configuration for these should be quite simple once we have the XC3000.

## Disclaimer

This project is still under development;
 some parts may not yet be fully functional, and existing interfaces,
 toolflows, and conventions may be broken without prior notice.

## Documentation

- [XC3000](doc/XC3000/)
    - [IOBs](doc/XC3000/IOB.md)
    - [CLBs](doc/XC3000/CLB.md)
    - [Routing](doc/XC3000/ROUTING.md)

## Goals

1. General understanding of the XC3000 architecture.
    - LCA format
    - CLBs configuration and options
        - fuzz connection
    - IOBs configuration and options
        - fuzz connections/PAD to IOB mapping
    - Routing Resources (local, long)
        - fuzz connections

2. YOSYS synthesis
    - Synthesis script
    - Primitives / Mapping
    - verilog2xnf script
    - PNR using XACT

3. NEXTPNR target
    - using the viaduct api, as himbaechel has problems with bidirectional wires between tiles.
    - convert the pnr-netlist to lca
    - use XACT to generate the bitstream

4. Bitstream reverse engineering
    - lca parser(so that we can compare our output to XACTs bitstream)
    - First start with a simple lookup-table based implementation:
        - Look at the configuration, flip the bits in an empty bitstream and the compare with XACT output
    - Eventually reason about each bits actual purpose

## Copyright

Tobias Senti, November 2024
