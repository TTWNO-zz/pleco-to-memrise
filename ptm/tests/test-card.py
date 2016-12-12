"""Test Card class."""

import unittest
from ptm.card import Card


def invalid_test_case():
    """Invalid test case, int instead of str."""
    return Card(1)


def invalid_test_case2():
    """Invalid test case int instae of str."""
    return Card("", "", "", 2)


class CardTests(unittest.TestCase):
    """Unittest for Card class."""

    def test_card_eq(self):
        """Test card eq method workd properly."""
        c1 = Card("青草", "青草", "qing1cao3", "cing1 cou2")
        c2 = Card("青草", "青草", "qing1cao3", "cing1 cou2")

        self.assertTrue(c1 == c2)

    def test_fails_on_invalid_input(self):
        """Test for fail on invalid case."""
        self.assertRaises(ValueError, invalid_test_case)
        self.assertRaises(ValueError, invalid_test_case2)
