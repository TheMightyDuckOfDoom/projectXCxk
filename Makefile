# Tobias Senti <git@tsenti.li>


DEVICE = 2064
PACKAGE = PC68
SPEED = -70

LCA2BIT = ./lca2bit.py
PARSE = ./parse.py --device $(DEVICE)
DESIGNS_DIR = designs

all: EMPTY

EMPTY:
	rm -f $(DESIGNS_DIR)/*
	echo "Version 2" > $(DESIGNS_DIR)/$@.lca
	echo "Design ${DEVICE}${PACKAGE}" >> $(DESIGNS_DIR)/$@.lca
	echo "Speed  ${SPEED}" >> $(DESIGNS_DIR)/$@.lca
	echo "Programorder On" >> $(DESIGNS_DIR)/$@.lca
	$(LCA2BIT) $@
	$(PARSE) designs/$@.BIT

IOB: IO_PAD = P5
IOB:
	rm -f $(DESIGNS_DIR)/$@.lca
	echo "Version 2" > $(DESIGNS_DIR)/$@.lca
	echo "Design ${DEVICE}${PACKAGE}" >> $(DESIGNS_DIR)/$@.lca
	echo "Speed  ${SPEED}" >> $(DESIGNS_DIR)/$@.lca
	echo "Programorder On" >> $(DESIGNS_DIR)/$@.lca

	echo "Nameblk ${IO_PAD} P3IN" >> $(DESIGNS_DIR)/$@.lca
	echo "Editblk ${IO_PAD}" >> $(DESIGNS_DIR)/$@.lca
	echo "Base IO" >> $(DESIGNS_DIR)/$@.lca
	echo "Config I:Q BUF:" >> $(DESIGNS_DIR)/$@.lca
	echo "Endblk" >> $(DESIGNS_DIR)/$@.lca
	$(LCA2BIT) $@
	$(PARSE) designs/$@.BIT

clean:
	rm -f designs/*
