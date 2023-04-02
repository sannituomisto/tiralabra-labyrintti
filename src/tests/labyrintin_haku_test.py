import unittest
from labyrintin_hakeminen import labyrintin_haku


class TestLabyrintinHaku(unittest.TestCase):
    def setUp(self):
        self.labyrintin_nro1 = 1
        self.labyrintin_nro2 = 6

    def test_20x20_labyrintin_haku_onnistuu(self):
        labyrintti = labyrintin_haku(self.labyrintin_nro1)

        self.assertEqual(len(labyrintti[0]), 20)
        self.assertEqual(len(labyrintti), 20)

    def test_100x100_labyrintin_haku_onnistuu(self):
        labyrintti = labyrintin_haku(self.labyrintin_nro2)

        self.assertEqual(len(labyrintti[0]), 100)
        self.assertEqual(len(labyrintti), 100)
