fuzz_iob:
	./fuzzer/fuzzer.py --target iob-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD1 --split_end PAD18 &
	./fuzzer/fuzzer.py --target iob-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD19 --split_end PAD37 &
	./fuzzer/fuzzer.py --target iob-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD38 --split_end PAD56 &
	./fuzzer/fuzzer.py --target iob-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD57 --split_end PAD75 &
	./fuzzer/fuzzer.py --target iob-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD76 --split_end PAD94 &
	./fuzzer/fuzzer.py --target iob-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD95 --split_end PAD113 &
	./fuzzer/fuzzer.py --target iob-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD114 --split_end PAD132 &
	./fuzzer/fuzzer.py --target iob-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start PAD133 --split_end PAD144 &

fuzz_clb:
	./fuzzer/fuzzer.py --target clb-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start A --split_end A &
	./fuzzer/fuzzer.py --target clb-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start B --split_end B &
	./fuzzer/fuzzer.py --target clb-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start C --split_end C &
	./fuzzer/fuzzer.py --target clb-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start D --split_end D &
	./fuzzer/fuzzer.py --target clb-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start E --split_end E &
                                                                                                                                      
	./fuzzer/fuzzer.py --target clb-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start F --split_end F &
	./fuzzer/fuzzer.py --target clb-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start G --split_end G &
	./fuzzer/fuzzer.py --target clb-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start H --split_end H &
	./fuzzer/fuzzer.py --target clb-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start I --split_end I &
	./fuzzer/fuzzer.py --target clb-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start J --split_end J &
                                                                                                                                      
	./fuzzer/fuzzer.py --target clb-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start K --split_end K &
	./fuzzer/fuzzer.py --target clb-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start L --split_end L &
	./fuzzer/fuzzer.py --target clb-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start M --split_end M &
	./fuzzer/fuzzer.py --target clb-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start N --split_end N &
	./fuzzer/fuzzer.py --target clb-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start O --split_end O &
                                                                                                                                      
	./fuzzer/fuzzer.py --target clb-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start P --split_end P &
	./fuzzer/fuzzer.py --target clb-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start Q --split_end Q &
	./fuzzer/fuzzer.py --target clb-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start R --split_end R &
	./fuzzer/fuzzer.py --target clb-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start S --split_end S &
	./fuzzer/fuzzer.py --target clb-local-long-pips --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start T --split_end T &

fuzz_magic:
	./fuzzer/fuzzer.py --target magic-connections --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start A --split_end A &
	./fuzzer/fuzzer.py --target magic-connections --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start B --split_end B &
	./fuzzer/fuzzer.py --target magic-connections --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start C --split_end C &
	./fuzzer/fuzzer.py --target magic-connections --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start D --split_end D &
	./fuzzer/fuzzer.py --target magic-connections --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start E --split_end E &

	./fuzzer/fuzzer.py --target magic-connections --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start F --split_end F &
	./fuzzer/fuzzer.py --target magic-connections --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start G --split_end G &
	./fuzzer/fuzzer.py --target magic-connections --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start H --split_end H &
	./fuzzer/fuzzer.py --target magic-connections --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start I --split_end I &
	./fuzzer/fuzzer.py --target magic-connections --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start J --split_end J &

	./fuzzer/fuzzer.py --target magic-connections --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start K --split_end K &
	./fuzzer/fuzzer.py --target magic-connections --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start L --split_end L &
	./fuzzer/fuzzer.py --target magic-connections --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start M --split_end M &
	./fuzzer/fuzzer.py --target magic-connections --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start N --split_end N &
	./fuzzer/fuzzer.py --target magic-connections --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start O --split_end O &

	./fuzzer/fuzzer.py --target magic-connections --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start P --split_end P &
	./fuzzer/fuzzer.py --target magic-connections --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start Q --split_end Q &
	./fuzzer/fuzzer.py --target magic-connections --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start R --split_end R &
	./fuzzer/fuzzer.py --target magic-connections --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start S --split_end S &
	./fuzzer/fuzzer.py --target magic-connections --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start T --split_end T &

fuzz_magic_bitstream:
	./fuzzer/fuzzer.py --target magic-bitstream --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start A --split_end A &
	./fuzzer/fuzzer.py --target magic-bitstream --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start B --split_end B &
	./fuzzer/fuzzer.py --target magic-bitstream --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start C --split_end C &
	./fuzzer/fuzzer.py --target magic-bitstream --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start D --split_end D &
	./fuzzer/fuzzer.py --target magic-bitstream --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start E --split_end E &

	./fuzzer/fuzzer.py --target magic-bitstream --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start F --split_end F &
	./fuzzer/fuzzer.py --target magic-bitstream --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start G --split_end G &
	./fuzzer/fuzzer.py --target magic-bitstream --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start H --split_end H &
	./fuzzer/fuzzer.py --target magic-bitstream --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start I --split_end I &
	./fuzzer/fuzzer.py --target magic-bitstream --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start J --split_end J &

	./fuzzer/fuzzer.py --target magic-bitstream --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start K --split_end K &
	./fuzzer/fuzzer.py --target magic-bitstream --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start L --split_end L &
	./fuzzer/fuzzer.py --target magic-bitstream --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start M --split_end M &
	./fuzzer/fuzzer.py --target magic-bitstream --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start N --split_end N &
	./fuzzer/fuzzer.py --target magic-bitstream --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start O --split_end O &

	./fuzzer/fuzzer.py --target magic-bitstream --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start P --split_end P &
	./fuzzer/fuzzer.py --target magic-bitstream --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start Q --split_end Q &
	./fuzzer/fuzzer.py --target magic-bitstream --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start R --split_end R &
	./fuzzer/fuzzer.py --target magic-bitstream --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start S --split_end S &
	./fuzzer/fuzzer.py --target magic-bitstream --device $(DEVICE) --package $(PACKAGE) --speed $(SPEED) --split_start T --split_end T &

merge_fuzz:
#ls -v ./results/${DEVICE}${PACKAGE}_CLB_LOCAL_LONG_PIPS_*.txt | xargs cat > ./results/${DEVICE}${PACKAGE}_CLB_LOCAL_LONG_PIPS.txt
#ls -v ./results/${DEVICE}${PACKAGE}_IOB_LOCAL_LONG_PIPS_*.txt | xargs cat > ./results/${DEVICE}${PACKAGE}_IOB_LOCAL_LONG_PIPS.txt
#ls -v ./results/${DEVICE}${PACKAGE}_IOB_MAPPING_*.txt | xargs cat > ./results/${DEVICE}${PACKAGE}_IOB_MAPPING.txt
#ls -v ./results/${DEVICE}${PACKAGE}_MAGIC_CONNECTIONS_*.txt | xargs cat > ./results/${DEVICE}${PACKAGE}_MAGIC_CONNECTIONS.txt
#ls -v ./results/${DEVICE}${PACKAGE}_MAGIC_CONNECTIONS_*.txt | xargs cat > ./results/${DEVICE}${PACKAGE}_MAGIC_BITSTREAM.txt

clean_fuzz:
	rm -f ./results/${DEVICE}${PACKAGE}_CLB_LOCAL_LONG_PIPS_*.txt
	rm -f ./results/${DEVICE}${PACKAGE}_IOB_LOCAL_LONG_PIPS_*.txt
	rm -f ./results/${DEVICE}${PACKAGE}_IOB_MAPPING_*.txt
	rm -f ./results/${DEVICE}${PACKAGE}_MAGIC_CONNECTIONS_*.txt
	rm -f ./results/${DEVICE}${PACKAGE}_MAGIC_BITSTREAM_*.txt
