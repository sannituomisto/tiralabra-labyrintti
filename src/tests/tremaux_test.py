import unittest
from unittest.mock import Mock
from tremaux import Tremaux


class TestTremaux(unittest.TestCase):
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
        self.Tre = Tremaux(
            self.labyrinth, self.pygame_mock, self.size, is_test=True)

    def test_tremaux_find_one_solved_path(self):
        result_from_algorithm = self.Tre.tremaux()
        result1 = [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1),
                   (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)]
        result2 = [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4),
                   (4, 5), (5, 5), (6, 5), (6, 6), (6, 7), (6, 8), (7, 8), (8, 8)]
        self.assertTrue(result_from_algorithm, result1 or result2)

    def test_find_start_and_end_block(self):
        result_from_algorithm = self.Tre.start_and_end_block()
        result = ((0, 1), (9, 8))
        self.assertEqual(result_from_algorithm, result)

    def test_finished_is_true(self):
        result_from_algorithm = self.Tre.start_tremaux()
        self.assertEqual(result_from_algorithm, True)
