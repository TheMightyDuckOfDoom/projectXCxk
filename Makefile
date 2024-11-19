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

include fuzz_split.mk

clean:
	rm -rf designs
	mkdir -p designs
	rm -f parser.out
	rm -f parsetab.py
