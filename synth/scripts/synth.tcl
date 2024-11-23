yosys -import

set LUT_K 5

yosys read_verilog -lib [file dirname [file normalize $argv0]]/../scripts/prims.v
yosys read_verilog [lindex $argv 0]
hierarchy -check -top [lindex $argv 1]
yosys proc
flatten
tribuf -logic
deminout
synth -run coarse
memory_map
opt -full
iopadmap -bits -inpad IBUF O:I -outpad OBUF I:O
stat
techmap -map +/techmap.v
opt -full
dfflegalize -cell \$_DFF_P_ x -cell \$_DFFE_PP_ x
# -cell \$_SDFF_PN0_ x -cell \$_SDFFE_PN0P_ x
stat
abc9 -lut $LUT_K
clean
techmap -D LUT_K=$LUT_K -map [file dirname [file normalize $argv0]]/../scripts/cells_map.v
opt_merge -share_all
splitnets -ports
yosys rename -scramble-name
clean -purge
stat
hierarchy -check
stat

if {[llength $argv] > 2} {
  yosys write_json [lindex $argv 2]/[lindex $argv 1]_synth.json
  yosys write_verilog [lindex $argv 2]/[lindex $argv 1]_synth.v
} else {
  yosys write_json ./out/[lindex $argv 1]_synth.json
  yosys write_verilog ./out/[lindex $argv 1]_synth.v
}
