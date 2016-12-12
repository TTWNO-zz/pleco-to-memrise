"""PlecoXMLExport class."""
import xml.etree.ElementTree as ET
from ptm import Card


class PlecoXMLExport:
    """PlecoXMLExport takes a Pleco XML file, and retrives card data."""

    def __init__(self, xml_data):
        """Create PlecoXMLExport object."""
        if not isinstance(xml_data, str):
            ValueError(
                "file_name must be type str, but is type {0}".format(
                    type(xml_data)))

        self.xml_data = xml_data
        self.cards = []
        self._generate_cards()

    def _generate_cards(self):
        """Generate cards from self.xml_data."""
        root = ET.fromstring(self.xml_data)
        for card in root.iter('card'):
            entry = card.find('entry')

            simp = entry.findall("headword[@charset='sc']")[0].text
            trad = entry.findall("headword[@charset='tc']")[0].text
            pinyin = entry.findall("pron[@type='hypy']")[0].text
            try:
                canto = entry.findall("cantopron")[0].text
            except IndexError:
                canto = ""
            english = entry.findall("defn")[0].text

            self.cards.append(
                Card(simp, trad, pinyin, canto=canto, defn=english))

    def get_cards(self):
        """Return generated cards."""
        return self.cards
