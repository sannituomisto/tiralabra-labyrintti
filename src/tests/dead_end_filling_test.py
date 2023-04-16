import unittest
from unittest.mock import Mock, ANY
from dead_end_filling import DeadEndFilling
from ikkuna import PygameIkkuna


class TestDeadEndFilling(unittest.TestCase):
    def setUp(self):
        self.labyrintti = [['@', '.', '@', '@', '@', '@', '@', '@', '@', '@'],
                           ['@', '.', '@', '@', '.', '.', '.', '.', '.', '@'],
                           ['@', '.', '.', '@', '.', '@', '@', '@', '.', '@'],
                           ['@', '.', '@', '@', '.', '@', '.', '@', '@', '@'],
                           ['@', '.', '.', '.', '.', '.', '.', '.', '.', '@'],
                           ['@', '.', '@', '@', '@', '.', '@', '@', '@', '@'],
                           ['@', '.', '@', '.', '.', '.', '.', '.', '.', '@'],
                           ['@', '.', '@', '@', '@', '@', '@', '@', '.', '@'],
                           ['@', '.', '.', '.', '.', '.', '.', '.', '.', '@'],
                           ['@', '@', '@', '@', '@', '@', '@', '@', '.', '@']]
        self.koko = 10
        self.ikkuna_mock = Mock()
        self.DeF = DeadEndFilling(
            self.labyrintti, 10, 60, ANY, self.ikkuna_mock)

    def test_loytaa_umpikujat(self):
        umpikujat = self.DeF.etsi_umpikujat()
        vastaus = [(2, 2), (2, 8), (3, 6), (6, 3), (4, 8)]
        self.assertEqual(sorted(umpikujat), sorted(vastaus))

    def test_osaa_tayttaa_umpikujat(self):
        umpikujat = self.DeF.etsi_umpikujat()
        umpikujien_kujat = self.DeF.taytetaan_umpikujat(umpikujat)
        vastaus = [(2, 2), (2, 8), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4),
                   (2, 4), (3, 4), (3, 6), (4, 8), (4, 7), (4, 6), (6, 3), (6, 4)]
        self.assertEqual(sorted(umpikujien_kujat), sorted(vastaus))
