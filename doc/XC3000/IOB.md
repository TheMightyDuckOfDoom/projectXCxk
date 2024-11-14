# Xilinx XC3000 IOB

## Pins

- Inputs -> to IOB
    - O - data to send to PAD
    - T - tristate enable
- Outputs -> from IOB
    - I - data from PAD
    - Q - data from PAD stored in latch/ff
- Clocks -> to IOB:
    - IK - clock for input latch/ff
    - OK - clock for output latch/ff

## Configuration

- LCA Base
    - is always 'IO'

- IN - settings for data from PAD -> IOB -> I, Q
    - I - enable input
    - IQ - enable input latch/ff
    - Modifiers
        - FF - set latch/ff to ff
        - LATCH - set latch/ff to latch
        - PULLUP - enable pullup -> only allowed on inputs
        - IKNOT - invert IK -> needs to be the same for the whole die edge, only makes sense with IQ

- OUT - settings for data from O -> IOB -> PAD
    - O, OQ - output or output from latch/ff
    - Modifiers
        - NOT - invert output
        - FAST - high slew rate
        - OKNOT - invert OK -> needs to be the same for the whole die edge, only makes sense with OQ

- TR - settings for tristate
    - T - use tristate output
    - Modifiers
        - NOT - invert tristate enable

## Bitstream

The following is listed in the datasheet:
- Logic inversion (O:NOT, OQ:NOT) is controlled by a single program bit per IOB
- The tristate buffer is either On, Off or controlled by the T input. If T is high, output is disabled -> in thristate. If it is zero the buffer is enabled and the pin is active.
- Inversion of the tristate control-logic is controlled by an additional configuration bit.
- Direct or registerd output is selectable for each IOB. OK connects to two long lines along the die edge(which can be inverted, but for all IOBs along the die edge, as the two lines are shared)
- FAST enables higher transition speeds
- internal pullup is enable by default

## Example LCA

    Nameblk P84 P84IOB
    Editblk P84
    Base IO
    Config IN:I:IQ:LATCH: OUT:O:NOT TRI:T
    Endblk
