#!/usr/bin/env bash
set -ex
yosys -p "tcl ./scripts/synth.tcl ~/servisia/out/servisia.v servisia"
