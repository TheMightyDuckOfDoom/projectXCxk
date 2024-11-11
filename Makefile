# Tobias Senti <git@tsenti.li>

LCA2BIT = ./lca2bit.py
PARSE = ./parse.py
DESIGNS_DIR = designs

all: EMPTY

EMPTY:
	echo "Version 2" > $(DESIGNS_DIR)/$@.lca
	echo "Design 2064PC68" >> $(DESIGNS_DIR)/$@.lca
	echo "Speed -70" >> $(DESIGNS_DIR)/$@.lca
	echo "Programorder On" >> $(DESIGNS_DIR)/$@.lca
	$(LCA2BIT) $@
	$(PARSE) designs/$@.BIT

IOB: IO_PAD = P5
IOB:
	echo "Version 2" > $(DESIGNS_DIR)/$@.lca
	echo "Design 2064PC68" >> $(DESIGNS_DIR)/$@.lca
	echo "Speed -70" >> $(DESIGNS_DIR)/$@.lca
	echo "Programorder On" >> $(DESIGNS_DIR)/$@.lca

	echo "Nameblk ${IO_PAD} P3IN" >> $(DESIGNS_DIR)/$@.lca
	echo "Editblk ${IO_PAD}" >> $(DESIGNS_DIR)/$@.lca
	echo "Base IO" >> $(DESIGNS_DIR)/$@.lca
	echo "Config I:Q BUF:OFF" >> $(DESIGNS_DIR)/$@.lca
	echo "Endblk" >> $(DESIGNS_DIR)/$@.lca
	$(LCA2BIT) $@
	$(PARSE) designs/$@.BIT

clean:
	rm -f designs/*
