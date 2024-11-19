FUZZ_IOB=iob-local-long-pips iob-direct-pips
FUZZ_ROW_MINUS_ONE=clb-local-long-pips 
FUZZ_ROW=magic-connections magic-bitstream local-long-pips
RESULT_FOLDER=$(DEVICE)$(PACKAGE)

$(RESULT_FOLDER):
	mkdir -p ./results/$(RESULT_FOLDER)

$(FUZZ_IOB): $(RESULT_FOLDER)
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD1 --split_end PAD18 &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD19 --split_end PAD37 &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD38 --split_end PAD56 &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD57 --split_end PAD75 &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD76 --split_end PAD94 &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD95 --split_end PAD113 &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD114 --split_end PAD132 &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD133 --split_end PAD144 &

$(FUZZ_ROW_MINUS_ONE): $(RESULT_FOLDER)
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start A --split_end A &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start B --split_end B &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start C --split_end C &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start D --split_end D &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start E --split_end E &

	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start F --split_end F &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start G --split_end G &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start H --split_end H &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start I --split_end I &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start J --split_end J &

	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start K --split_end K &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start L --split_end L &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start M --split_end M &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start N --split_end N &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start O --split_end O &

	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start P --split_end P &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start Q --split_end Q &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start R --split_end R &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start S --split_end S &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start T --split_end T &

$(FUZZ_ROW): $(RESULT_FOLDER)
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start A --split_end A &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start B --split_end B &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start C --split_end C &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start D --split_end D &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start E --split_end E &

	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start F --split_end F &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start G --split_end G &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start H --split_end H &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start I --split_end I &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start J --split_end J &

	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start K --split_end K &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start L --split_end L &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start M --split_end M &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start N --split_end N &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start O --split_end O &

	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start P --split_end P &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start Q --split_end Q &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start R --split_end R &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start S --split_end S &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start T --split_end T &

	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start U --split_end U &

merge_fuzz: $(RESULT_FOLDER)
#ls -v ./results/${DEVICE}${PACKAGE}/CLB_LOCAL_LONG_PIPS_*.txt | xargs cat > ./results/${DEVICE}${PACKAGE}/CLB_LOCAL_LONG_PIPS.txt
#ls -v ./results/${DEVICE}${PACKAGE}/IOB_LOCAL_LONG_PIPS_*.txt | xargs cat > ./results/${DEVICE}${PACKAGE}/IOB_LOCAL_LONG_PIPS.txt
#ls -v ./results/${DEVICE}${PACKAGE}/IOB_MAPPING_*.txt | xargs cat > ./results/${DEVICE}${PACKAGE}/IOB_MAPPING.txt
#ls -v ./results/${DEVICE}${PACKAGE}/MAGIC_CONNECTIONS_*.txt | xargs cat > ./results/${DEVICE}${PACKAGE}/MAGIC_CONNECTIONS.txt
#ls -v ./results/${DEVICE}${PACKAGE}/MAGIC_BITSTREAM_*.txt | xargs cat > ./results/${DEVICE}${PACKAGE}/MAGIC_BITSTREAM.txt
#ls -v ./results/${DEVICE}${PACKAGE}/LOCAL_LONG_PIPS_*.txt | xargs cat > ./results/${DEVICE}${PACKAGE}/LOCAL_LONG_PIPS.txt
#ls -v ./results/${DEVICE}${PACKAGE}/IOB_DIRECT_*.txt | xargs cat > ./results/${DEVICE}${PACKAGE}/IOB_DIRECT.txt

clean_fuzz:
	rm -f ./results/${DEVICE}${PACKAGE}/CLB_LOCAL_LONG_PIPS_*.txt
	rm -f ./results/${DEVICE}${PACKAGE}/IOB_LOCAL_LONG_PIPS_*.txt
	rm -f ./results/${DEVICE}${PACKAGE}/IOB_MAPPING_*.txt
	rm -f ./results/${DEVICE}${PACKAGE}/MAGIC_CONNECTIONS_*.txt
	rm -f ./results/${DEVICE}${PACKAGE}/MAGIC_BITSTREAM_*.txt
	rm -f ./results/${DEVICE}${PACKAGE}/LOCAL_LONG_PIPS_*.txt
	rm -f ./results/${DEVICE}${PACKAGE}/IOB_DIRECT_*.txt
