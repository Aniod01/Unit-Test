import unittest

from app.cerc import Cerc


class TestCerc(unittest.TestCase):

    def test_arie(self):
        cerc1 = Cerc(5)
        expected_arie = cerc1.get_arie()
        actual_arie = 78.5
        self.assertEqual(expected_arie, actual_arie)

    def test_diametru(self):
        cerc2 = Cerc(6)
        expected_diamteru = cerc2.get_diametru()
        actual_diamteru = 12
        self.assertEqual(expected_diamteru,actual_diamteru)
