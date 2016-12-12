"""Card class for tempstoring pleco cards."""


class Card:
    """Card class for pleco cards."""

    def __init__(self, simp="", trad="", pinyin="",
                 canto="", zhuyin="", defn=""):
        """Initialize Card."""
        self.trad = trad
        self.simp = simp
        self.pinyin = pinyin
        self.canto = canto
        self.zhuyin = zhuyin
        self.defn = defn
        self.check_rep()

    def get_traditional(self):
        """Return traditional text."""
        return self.trad

    def get_simplified(self):
        """Return simplified text."""
        return self.simp

    def get_canto_pron(self):
        """Return canto pronounceation."""
        return self.canto

    def get_zhuyin(self):
        """Return zhuyin pronounceation."""
        return self.zhuyin

    def get_pinyin(self):
        """Return pinyin pronounceation."""
        return self.pinyin

    def get_defn(self):
        """Return defenition."""
        return self.defn

    def __eq__(self, other):
        """Check if cards are equal."""
        if not isinstance(other, Card):
            raise ValueError(
                "Cannot compare a Card object with a {0}".format(
                    type(other)))

        return (self.trad == other.trad and
                self.simp == other.simp and
                self.zhuyin == other.zhuyin and
                self.canto == other.canto and
                self.pinyin == other.pinyin)

    def __str__(self):
        """Retrun representative string."""
        return "TC: {0}\nSC: {1}\nPY: {2}\nCP: {3}\nZY: {4}\nEN: {5}".format(
            self.trad, self.simp, self.pinyin,
            self.canto, self.zhuyin, self.defn
        )

    def check_rep(self):
        """Check representation, error if not represented correctly."""
        if not isinstance(self.simp, str):
            raise ValueError(
                "simp argument must be of type str, but is {0}".format(
                    type(self.simp)))

        if not isinstance(self.trad, str):
            raise ValueError(
                "trad argument must be of type str, but is {0}".format(
                    type(self.trad)))

        if not isinstance(self.pinyin, str):
            raise ValueError(
                "pinyin argument must be of type str, but is {0}".format(
                    type(self.pinyin)))

        if not isinstance(self.zhuyin, str):
            raise ValueError(
                "zhuyin argument must be of type str, but is {0}".format(
                    type(self.zhuyin)))

        if not isinstance(self.canto, str):
            raise ValueError(
                "canto argument must be of type str, but is {0}".format(
                    type(self.canto)))

        if not isinstance(self.defn, str):
            raise ValueError(
                "Defenition (defn) must be of type str, but is {0}".format(
                    type(self.defn)))
