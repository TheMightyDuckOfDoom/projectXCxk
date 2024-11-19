DEVICE?=3090
PACKAGE?=PC84

target?=mc14500
target_src?=examples/$(target).v

#target=servisia
#target_src=~/servisia/out/servisia.v

all: synth v2xnf implement

synth:
	mkdir -p out
	yosys -p "tcl ./scripts/synth.tcl $(target_src) $(target)"

v2xnf:
	./verilog2xnf.py ./out/$(target)_synth.v ./out/$(target).xnf --device $(DEVICE) --package $(PACKAGE)

implement:
	mkdir -p out
	echo 'C:' > out/$(target).bat
	echo 'set PATH=%PATH%;D:\' >> out/$(target).bat
	echo 'set XACT=D:\' >> out/$(target).bat
	echo 'XMAKE -X -P ${DEVICE}${PACKAGE} $(target).xnf > xmake.log' >> out/$(target).bat
	cd out && SDL_VIDEODRIVER=dummy dosbox $(target).bat -c "MOUNT D: ../../XACT" -exit > /dev/null

clean:
	rm -rf out
