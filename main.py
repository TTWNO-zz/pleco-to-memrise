"""_ is a test, lol!."""

import sys
from ptm import PlecoXMLExport

f = open(sys.argv[1])
x = f.read()
f.close()
p = PlecoXMLExport(x)
c = p.get_cards()
for card in c:
    print("{0}\t{1}\t{2}".format(card.get_traditional(), card.get_pinyin(), card.get_defn()))
