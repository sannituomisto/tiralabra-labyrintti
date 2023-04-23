import unittest
from unittest.mock import Mock
from dead_end_filling import DeadEndFilling


class TestDeadEndFilling(unittest.TestCase):
    def setUp(self):
        self.labyrinth = [['@', '.', '@', '@', '@', '@', '@', '@', '@', '@'],
                          ['@', '.', '@', '@', '.', '.', '.', '.', '.', '@'],
                          ['@', '.', '.', '@', '.', '@', '@', '@', '.', '@'],
                          ['@', '.', '@', '@', '.', '@', '.', '@', '@', '@'],
                          ['@', '.', '.', '.', '.', '.', '.', '.', '.', '@'],
                          ['@', '.', '@', '@', '@', '.', '@', '@', '@', '@'],
                          ['@', '.', '@', '.', '.', '.', '.', '.', '.', '@'],
                          ['@', '.', '@', '@', '@', '@', '@', '@', '.', '@'],
                          ['@', '.', '.', '.', '.', '.', '.', '.', '.', '@'],
                          ['@', '@', '@', '@', '@', '@', '@', '@', '.', '@']]
        self.size = 10
        self.pygame_mock = Mock()
        self.DeF = DeadEndFilling(
            self.labyrinth, self.pygame_mock, self.size, is_test=True)

    def test_find_dead_ends(self):
        dead_ends = self.DeF.find_dead_ends()
        result = [(2, 2), (2, 8), (3, 6), (6, 3), (4, 8)]
        self.assertEqual(sorted(dead_ends), sorted(result))

    def test_fill_dead_ends(self):
        dead_ends = self.DeF.find_dead_ends()
        dead_end_paths = self.DeF.fill_dead_ends(dead_ends)
        result = [(2, 2), (2, 8), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4),
                  (2, 4), (3, 4), (3, 6), (4, 8), (4, 7), (4, 6), (6, 3), (6, 4)]
        self.assertEqual(sorted(dead_end_paths), sorted(result))
