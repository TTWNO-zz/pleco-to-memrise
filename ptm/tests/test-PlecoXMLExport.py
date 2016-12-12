"""Test for problems with PlecoXMLExport."""

import unittest
from ptm import Card
from ptm import PlecoXMLExport

f = open('data/pleco-test.xml')
xml_data = f.read()
f.close()


class TestPlecoXMLExport(unittest.TestCase):
    """Tests for PlecoXMLExport."""

    def test_get_cards(self):
        """Test get_cards returns the correct cards."""
        pxml = PlecoXMLExport(xml_data)

        c1 = Card(simp="野地", trad="野地", pinyin="ye3di4",
                  canto="je5 dei6", defn="wild country; wilderness")
        c2 = Card(simp="青草", trad="青草", pinyin="qing1cao3",
                  defn="green grass")

        self.assertEqual(str(pxml.get_cards()[0]), str(c2))
        self.assertEqual(str(pxml.get_cards()[1]), str(c1))
