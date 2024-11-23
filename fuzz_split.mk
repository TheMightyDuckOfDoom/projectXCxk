FUZZ_IOB=iob-local-long-pips iob-direct-pips
FUZZ_ROW=magic-connections local-long-pips clb-local-long-pips clb-direct-pips
RESULT_FOLDER=$(DEVICE)
TIMESTAMP=$(shell date +%Y_%m_%d_%H_%M_%S)
ARGS=

$(RESULT_FOLDER):
	mkdir -p ./results/$(RESULT_FOLDER)
	mkdir -p ./results/$(RESULT_FOLDER)/package

fuzz_all: $(FUZZ_IOB) $(FUZZ_ROW_MINUS_ONE) $(FUZZ_ROW)

fuzz_onlyiobmapping: ARGS=--onlyiobmapping
fuzz_onlyiobmapping: iob-local-long-pips

$(FUZZ_IOB): $(RESULT_FOLDER)
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD1   --split_end PAD8   $(ARGS) &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD9   --split_end PAD16  $(ARGS) &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD17  --split_end PAD24  $(ARGS) &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD25  --split_end PAD32  $(ARGS) &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD33  --split_end PAD40  $(ARGS) &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD41  --split_end PAD48  $(ARGS) &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD49  --split_end PAD56  $(ARGS) &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD57  --split_end PAD64  $(ARGS) &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD65  --split_end PAD72  $(ARGS) &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD73  --split_end PAD80  $(ARGS) &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD81  --split_end PAD88  $(ARGS) &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD89  --split_end PAD96  $(ARGS) &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD97  --split_end PAD104 $(ARGS) &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD105 --split_end PAD112 $(ARGS) &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD113 --split_end PAD120 $(ARGS) &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD121 --split_end PAD128 $(ARGS) &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD129 --split_end PAD136 $(ARGS) &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD137 --split_end PAD144 $(ARGS) &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD145 --split_end PAD152 $(ARGS) &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD153 --split_end PAD160 $(ARGS) &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD161 --split_end PAD168 $(ARGS) &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD169 --split_end PAD176 $(ARGS) &

$(FUZZ_ROW) magic-bitstream: $(RESULT_FOLDER)
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
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start V --split_end V &
	./fuzzer/fuzzer.py --target $@ --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start W --split_end W &

fuzz_backup: $(RESULT_FOLDER)
	mkdir -p ./results/.backup/
	cp ./results/$(RESULT_FOLDER) ./results/.backup/$(RESULT_FOLDER)_${TIMESTAMP} -r

merge_iobmapping: fuzz_backup
	ls -v ./results/${RESULT_FOLDER}/package/${PACKAGE}_IOB_MAPPING_*.txt | xargs cat > ./results/${RESULT_FOLDER}/package/${PACKAGE}_IOB_MAPPING.txt

merge_fuzz: fuzz_backup
	ls -v ./results/${RESULT_FOLDER}/CLB_LOCAL_LONG_PIPS_*.txt | xargs cat > ./results/${RESULT_FOLDER}/CLB_LOCAL_LONG_PIPS.txt
	ls -v ./results/${RESULT_FOLDER}/IOB_LOCAL_LONG_PIPS_*.txt | xargs cat > ./results/${RESULT_FOLDER}/IOB_LOCAL_LONG_PIPS.txt
	ls -v ./results/${RESULT_FOLDER}/package/${PACKAGE}_IOB_MAPPING_*.txt | xargs cat > ./results/${RESULT_FOLDER}/package/${PACKAGE}_IOB_MAPPING.txt
	ls -v ./results/${RESULT_FOLDER}/MAGIC_CONNECTIONS_*.txt | xargs cat > ./results/${RESULT_FOLDER}/MAGIC_CONNECTIONS.txt
#	ls -v ./results/${RESULT_FOLDER}/MAGIC_BITSTREAM_*.txt | xargs cat > ./results/${RESULT_FOLDER}/MAGIC_BITSTREAM.txt
	ls -v ./results/${RESULT_FOLDER}/LOCAL_LONG_PIPS_*.txt | xargs cat > ./results/${RESULT_FOLDER}/LOCAL_LONG_PIPS.txt
	ls -v ./results/${RESULT_FOLDER}/IOB_DIRECT_*.txt | xargs cat > ./results/${RESULT_FOLDER}/IOB_DIRECT.txt
	ls -v ./results/${RESULT_FOLDER}/CLB_DIRECT_*.txt | xargs cat > ./results/${RESULT_FOLDER}/CLB_DIRECT.txt

clean_fuzz: fuzz_backup
	rm -f ./results/${RESULT_FOLDER}/CLB_LOCAL_LONG_PIPS_*.txt
	rm -f ./results/${RESULT_FOLDER}/IOB_LOCAL_LONG_PIPS_*.txt
	rm -f ./results/${RESULT_FOLDER}/package/${PACKAGE}_IOB_MAPPING_*.txt
	rm -f ./results/${RESULT_FOLDER}/MAGIC_CONNECTIONS_*.txt
	rm -f ./results/${RESULT_FOLDER}/MAGIC_BITSTREAM_*.txt
	rm -f ./results/${RESULT_FOLDER}/LOCAL_LONG_PIPS_*.txt
	rm -f ./results/${RESULT_FOLDER}/IOB_DIRECT_*.txt
	rm -f ./results/${RESULT_FOLDER}/CLB_DIRECT_*.txt
