# Xilinx XC3000 CLB

A XC3000 CLB contains the following(from the Datasheet):
- five logic variable inputs: A, B, C, D and E
- a direct data in DI
- an enable clock EC
- a clock (invertible) K
- an asynchronous direct RESET RD
- two outputs X and Y

## Pins

- Inputs
    - A, B, C, D, E - Logic Variable Inputs
    - DI - Direct Data In
    - EC - Enable Clock
    - RD - Direct Reset (asynchronous)
    - K - Clock
- Outputs
    - X and Y

## Configuration

- LCA Base
    - F - LUT5 mode, any function of 5 inputs: 
        - F, G = func(A, [B, QX, QY], [C, QX, QY], D, E)
    - FG - 2x LUT4 mode, two functions of 4 inputs:
        - F = func(A, [B, QX, QY], [C, QX, QY], [D, E])
        - G = func(A, [B, QX, QY], [C, QX, QY], [D, E])
    - FGM - MUX between 2x LUT4:
        - func1 = func(A, [B, QX, QY], [C, QX, QY], D)
        - func2 = func(A, [B, QX, QY], [C, QX, QY], D)
        - F,G = E ? func2 : func1

- X - select X function
    - F, QX - LUT output F or FlipFlop QX
- Y - select Y function
    - G, QY - LUT output G or FlipFlop QY

- DX - select data input for FlipFlop QX
    - DI, F, G - Direct Data In, LUT output F or LUT output G

- DY - select data input for FlipFlop QY
    - DI, F, G - Direct Data In, LUT output F or LUT output G

- CLK - clock config, only makes sense if X:QX or Y:QY
    - K, K:NOT - either positive or negative clock for whole CLB

- RSTDIR - FlipFlop direct reset input used, only makes sense if X:QX or Y:QY
    - RD - use direct reset input

- ENCLK - clock enable
    - EC - use clock enable

- F - inputs for F function
    - A
    - B, QX or QY
    - C, QX or QY
    - D
    - E
- G - inputs for G function
    - A
    - B, QX, or QY
    - C, QX, or QY
    - D
    - E
