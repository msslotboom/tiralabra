import unittest
from connect4 import Connect4

class TestConnect4(unittest.TestCase):
	def setUp(self):
		self.game = Connect4()

	def test_playing_move_changes_board(self):
		self.game.play_move(1,1)
		correct_game_after_move = [[0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0],
				[0, 1, 0, 0, 0, 0, 0]]
		self.assertEqual(correct_game_after_move, self.game.table)

	def test_horizontal_win_detection_works(self):
		self.game.table = [[0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0],
				[1, 1, 1, 1, 0, 0, 0]]

		self.game.last_added = (5,0)
		result = self.game.calculate_winner()
		self.assertTrue(result)

	def test_vertical_win_detection_works(self):
		self.game.table = [[0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0],
				[1, 0, 0, 0, 0, 0, 0],
				[1, 0, 0, 0, 0, 0, 0],
				[1, 0, 0, 0, 0, 0, 0],
				[1, 0, 0, 0, 0, 0, 0]]
		self.game.last_added = (2, 0)
		result = self.game.calculate_winner()
		self.assertTrue(result)

	def test_diag_1_win_detection_works(self):
		self.game.table = [[0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 1, 0, 0, 0],
				[0, 0, 1, 0, 0, 0, 0],
				[0, 1, 0, 0, 0, 0, 0],
				[1, 0, 1, 1, 0, 0, 0]]

		self.game.last_added = (5,0)
		result = self.game.calculate_winner()
		self.assertTrue(result)

	def test_diag_2_win_detection_works(self):
		self.game.table = [[0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0],
				[0, 1, 0, 1, 0, 0, 0],
				[0, 0, 1, 0, 0, 0, 0],
				[0, 1, 0, 1, 0, 0, 0],
				[1, 0, 1, 1, 1, 0, 0]]

		self.game.last_added = (2,1)
		result = self.game.calculate_winner()
		self.assertTrue(result)