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

        self.labyrinth2 = [['@', '.', '@', '@', '@', '@', '@', '@', '@', '@'],
                           ['@', '.', '@', '@', '@', '@', '@', '@', '@', '@'],
                           ['@', '.', '@', '@', '@', '@', '@', '@', '@', '@'],
                           ['@', '.', '@', '@', '@', '@', '@', '@', '@', '@'],
                           ['@', '.', '.', '.', '.', '.', '@', '@', '@', '@'],
                           ['@', '.', '@', '@', '@', '.', '@', '@', '@', '@'],
                           ['@', '.', '@', '@', '@', '.', '.', '.', '.', '@'],
                           ['@', '.', '@', '@', '@', '@', '@', '@', '.', '@'],
                           ['@', '.', '.', '.', '.', '.', '.', '.', '.', '@'],
                           ['@', '@', '@', '@', '@', '@', '@', '@', '.', '@']]
        
        self.labyrinth3 = [['@', '.', '@', '@', '@', '@', '@', '@', '@', '@'],
                           ['@', '.', '@', '@', '@', '@', '@', '@', '@', '@'],
                           ['@', '.', '@', '@', '@', '@', '@', '@', '@', '@'],
                           ['@', '.', '@', '@', '@', '@', '@', '@', '@', '@'],
                           ['@', '.', '.', '.', '.', '.', '@', '@', '@', '@'],
                           ['@', '.', '@', '@', '@', '.', '@', '@', '@', '@'],
                           ['@', '.', '@', '@', '@', '.', '.', '@', '.', '@'],
                           ['@', '.', '@', '@', '@', '@', '@', '@', '.', '@'],
                           ['@', '.', '.', '.', '.', '.', '.', '@', '.', '@'],
                           ['@', '@', '@', '@', '@', '@', '@', '@', '.', '@']]

        self.solved_labyrinth = [['@', '.', '@', '@', '@', '@', '@', '@', '@', '@'],
                                 ['@', '.', '@', '@', '#', '#', '#', '#', '#', '@'],
                                 ['@', '.', '#', '@', '#', '@', '@', '@', '#', '@'],
                                 ['@', '.', '@', '@', '#', '@', '#', '@', '@', '@'],
                                 ['@', '.', '.', '.', '.', '.', '#', '#', '#', '@'],
                                 ['@', '.', '@', '@', '@', '.', '@', '@', '@', '@'],
                                 ['@', '.', '@', '#', '#', '.', '.', '.', '.', '@'],
                                 ['@', '.', '@', '@', '@', '@', '@', '@', '.', '@'],
                                 ['@', '.', '.', '.', '.', '.', '.', '.', '.', '@'],
                                 ['@', '@', '@', '@', '@', '@', '@', '@', '.', '@']]
        
        self.solved_labyrinth3 = [['@', '#', '@', '@', '@', '@', '@', '@', '@', '@'],
                           ['@', '#', '@', '@', '@', '@', '@', '@', '@', '@'],
                           ['@', '#', '@', '@', '@', '@', '@', '@', '@', '@'],
                           ['@', '#', '@', '@', '@', '@', '@', '@', '@', '@'],
                           ['@', '#', '#', '#', '#', '#', '@', '@', '@', '@'],
                           ['@', '#', '@', '@', '@', '#', '@', '@', '@', '@'],
                           ['@', '#', '@', '@', '@', '#', '#', '@', '#', '@'],
                           ['@', '#', '@', '@', '@', '@', '@', '@', '#', '@'],
                           ['@', '#', '#', '#', '#', '#', '#', '@', '#', '@'],
                           ['@', '@', '@', '@', '@', '@', '@', '@', '#', '@']]
        
        self.size = 10
        self.pygame_mock = Mock()
        self.DeF = DeadEndFilling(
            self.labyrinth, self.pygame_mock, self.size, is_test=True)
        self.DeF2 = DeadEndFilling(
            self.labyrinth2, self.pygame_mock, self.size, is_test=True)
        self.DeF3 = DeadEndFilling(
            self.labyrinth3, self.pygame_mock, self.size, is_test=True)

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

    def test_solved_labyrinth_is_correct(self):
        result = self.DeF.dead_end_filling()
        self.assertEqual(result, (True, self.solved_labyrinth))

    def test_do_not_find_dead_ends_if_not_dead_ends(self):
        dead_ends = self.DeF2.find_dead_ends()
        self.assertEqual(len(dead_ends), 0)

    def test_labyrinth_do_not_change_if_no_dead_ends(self):
        result = self.DeF2.dead_end_filling()
        self.assertEqual(result, (None, self.labyrinth2))

    def test_if_not_solution(self):
        result = self.DeF3.dead_end_filling()
        self.assertEqual(result, (True, self.solved_labyrinth3))
