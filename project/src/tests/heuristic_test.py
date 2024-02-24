import unittest
from heuristic import Heuristic
from connect4 import Connect4

class TestHeuristic(unittest.TestCase):
    def setUp(self):
        self.heuristic = Heuristic()
        self.game = Connect4()

    def test_sequence_with_zero_at_end_returns_one(self):
        sequence = [1, 1, 1, 0]
        result = self.heuristic.count_one_off_four_in_a_row(sequence)
        self.assertEqual(result[0], 1)

    def test_sequence_with_zero_in_middle_returns_one(self):
        sequence = [1, 0, 1, 1]
        result = self.heuristic.count_one_off_four_in_a_row(sequence)
        self.assertEqual(result[0], 1)

    def test_sequence_with_two_zeros_in_middle_returns_zero(self):
        sequence = [1, 0, 0, 1]
        result = self.heuristic.count_one_off_four_in_a_row(sequence)
        self.assertEqual(result[0], 0)

    def test_sequence_with_ones_then_zero_then_three_twos_returns_one(self):
        sequence = [1, 1, 0, 0, 2, 2, 2]
        result = self.heuristic.count_one_off_four_in_a_row(sequence)
        self.assertEqual(result[1], 1)

    def test_sequence_with_sequence_of_ones_then_twos_returns_one_for_both(self):
        sequence = [1, 1, 1, 0, 2, 2, 2]
        result = self.heuristic.count_one_off_four_in_a_row(sequence)
        self.assertEqual(result, (1, 1))

    def test_sequence_with_one_in_and_end_detects_two(self):
        sequence = [0, 1, 1, 1, 0]
        result = self.heuristic.count_one_off_four_in_a_row(sequence)
        self.assertEqual(result, (2, 0))

    def test_heuristic(self):
        self.game.table = [[0, 0, 0, 1, 0, 0, 0],
                                                      [0, 0, 0, 0, 0, 0, 0],
                                                      [0, 0, 0, 0, 0, 0, 0],
                                                      [0, 0, 1, 0, 0, 0, 0],
                                                      [0, 1, 0, 0, 1, 0, 0],
                                                      [1, 0, 0, 1, 0, 0, 0]]
        result = self.heuristic._calculate_heuristic(self.game)
        self.assertEqual(result, -100)

    def test_heuristic_finds_horizontal_with_empty_in_middle(self):
        self.game.table = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0],
                 [1, 1, 0, 1, 0, 0, 0]]

        result = self.heuristic._calculate_heuristic(self.game)
        self.assertEqual(result, -100)

    def test_no_count_horizontal_many_zeros(self):
        self.game.table = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0],
                 [2, 0, 2, 0, 0, 1, 1]]

        result = self.heuristic._calculate_heuristic(self.game)
        self.assertEqual(result, 0)

    def test_no_count_when_two_off_one_in_a_row_horizontally(self):
        self.game.table = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0],
                 [1, 1, 0, 0, 0, 0, 0]]
        result = self.heuristic._calculate_heuristic(self.game)
        self.assertEqual(result, 0)

    def test_find_sequence_start_zero_horizontal(self):
        self.game.table = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0],
                 [2, 0, 0, 0, 1, 1, 1]]
        result = self.heuristic._calculate_heuristic(self.game)
        self.assertEqual(result, -100)

    def test_find_sequence_with_zero_at_start(self):
        self.game.table = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0],
                 [0, 1, 1, 1, 2, 0, 0]]

        result = self.heuristic._calculate_heuristic(self.game)
        self.assertEqual(result, -100)

    def test_heuristc_finds_if_zero_in_front_and_empty_in_middle(self):
        self.game.table = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 1, 1, 0]]

        result = self.heuristic._calculate_heuristic(self.game)
        self.assertEqual(result, -100)

    def test_heuristic_finds_vertical(self):
        self.game.table = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1, 0, 0],
                 [1, 0, 2, 1, 0, 0, 0]]

        result = self.heuristic._calculate_heuristic(self.game)
        self.assertEqual(result, -100)

    def test_heuristic_no_find_blocked_horizontal(self):
        self.game.table = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0],
                 [1, 1, 2, 1, 0, 0, 0]]

        result = self.heuristic._calculate_heuristic(self.game)
        self.assertEqual(result, 0)

    def test_heuristic_finds_diag_start_on_column_zero(self):
        self.game.table = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 2, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 2, 0, 0, 0, 0, 0],
                 [2, 0, 0, 0, 1, 0, 0],
                 [2, 0, 0, 0, 1, 2, 1]]
        result = self.heuristic._calculate_heuristic(self.game)
        self.assertEqual(result, 100)

    def test_heuristic_finds_diag_not_starting_in_column_zero(self):
        self.game.table = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 2, 0, 0],
                 [0, 0, 0, 2, 1, 0, 0],
                 [2, 0, 2, 0, 1, 2, 1]]
        result = self.heuristic._calculate_heuristic(self.game)
        self.assertEqual(result, 100)

    def test_heuristic_finds_rising_starting_from_bottom_row(self):
        self.game.table = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0],
                 [0, 1, 0, 0, 1, 0, 0],
                 [1, 0, 0, 1, 0, 0, 0]]
        result = self.heuristic._calculate_heuristic(self.game)
        self.assertEqual(result, -100)
