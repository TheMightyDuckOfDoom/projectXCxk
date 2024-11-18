# Tobias Senti <git@tsenti.li>

DEVICE = 3090
PACKAGE = PC84
SPEED = -100

LCA2BIT = ./lca2bit.py
PARSE = ./parse.py --device $(DEVICE)
DESIGNS_DIR = designs

all: EMPTY

dosbox:
	dosbox -c "MOUNT D: ./XACT" -c "MOUNT C: ./" -c "C:" -c "set PATH=%PATH%;D:\\" -c "XACT -e test.lca"

EMPTY:
	rm -f $(DESIGNS_DIR)/$@.*
	echo "Version 2" > $(DESIGNS_DIR)/$@.lca
	echo "Design ${DEVICE}${PACKAGE}" >> $(DESIGNS_DIR)/$@.lca
	echo "Speed  ${SPEED}" >> $(DESIGNS_DIR)/$@.lca
	echo "Programorder On" >> $(DESIGNS_DIR)/$@.lca
	$(LCA2BIT) $@
	$(PARSE) designs/$@.BIT

fuzz_all: fuzz_iob fuzz_clb fuzz_magic

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

merge_fuzz:
#ls -v ./results/${DEVICE}${PACKAGE}_CLB_LOCAL_LONG_PIPS_*.txt | xargs cat > ./results/${DEVICE}${PACKAGE}_CLB_LOCAL_LONG_PIPS.txt
#ls -v ./results/${DEVICE}${PACKAGE}_IOB_LOCAL_LONG_PIPS_*.txt | xargs cat > ./results/${DEVICE}${PACKAGE}_IOB_LOCAL_LONG_PIPS.txt
#ls -v ./results/${DEVICE}${PACKAGE}_IOB_MAPPING_*.txt | xargs cat > ./results/${DEVICE}${PACKAGE}_IOB_MAPPING.txt
	ls -v ./results/${DEVICE}${PACKAGE}_MAGIC_CONNECTIONS_*.txt | xargs cat > ./results/${DEVICE}${PACKAGE}_MAGIC_CONNECTIONS.txt

clean_fuzz:
	rm -f ./results/${DEVICE}${PACKAGE}_CLB_LOCAL_LONG_PIPS_*.txt
	rm -f ./results/${DEVICE}${PACKAGE}_IOB_LOCAL_LONG_PIPS_*.txt
	rm -f ./results/${DEVICE}${PACKAGE}_IOB_MAPPING_*.txt
	rm -f ./results/${DEVICE}${PACKAGE}_MAGIC_CONNECTIONS_*.txt

clean:
	rm -f designs/*
	rm -f parser.out
	rm -f parsetab.py
