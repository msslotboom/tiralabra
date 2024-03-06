import unittest
from minimax import Minimax
from connect4 import Connect4


class TestMinimax(unittest.TestCase):
    def setUp(self) -> None:
        self.game = Connect4()
        self.algo = Minimax()

    def test_returns_winning_move_if_one_off_win(self):
        self.game.table = [[0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [2, 2, 2, 0, 0, 1, 0]]
        self.game.last_added = (5, 0)
        score, move = self.algo._minimax(
            self.game, 3, True, -100000000000, 100000000000)
        self.assertEqual(move, 3)
        self.assertEqual(score, 10000)

    def test_blocks_if_opponent_one_off_win(self):
        self.game.table = [[0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 1, 0],
                           [0, 0, 0, 0, 0, 1, 0],
                           [2, 0, 0, 0, 0, 1, 0]]
        self.game.last_added = (3, 5)
        print(self.game.table[5][2])
        score, move = self.algo._minimax(
            self.game, 2, True, -100000000000, 100000000000)
        self.assertEqual(move, 5)
        self.assertEqual(score, 0)
