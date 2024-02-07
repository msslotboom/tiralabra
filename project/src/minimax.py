from connect4 import Connect4
from copy import deepcopy
from random import choice

class Minimax():
	def __init__(self) -> None:
		self.game = Connect4()
		self.move_dict = {}

	# Heuristic: the higher, the better for the computer
	def _heuristic(self, game: Connect4):
		if game.calculate_winner():
			row, col = game.last_added
			if game.table[row][col] == 2:
				return 1
			return -1
		return 0

	def _minimax(self, game, depth, maximising):
		if depth == 0 or game.calculate_winner():
			return self._heuristic(game)
		if maximising:
			value = -5
			for i in range(len(game.table)):
				new_game = Connect4()
				new_game.table = deepcopy(game.table)
				if new_game.play_move(i, 2):
					value = max(value, self._minimax(new_game, depth-1, False))
			return value
		else:  # Minimising player
			value = 5
			for i in range(len(game.table)):
				new_game = Connect4()
				new_game.table = deepcopy(game.table)
				if new_game.play_move(i, 1):
					value = min(value, self._minimax(new_game, depth-1, True))
			return value

	def calculate_move(self, board: list, depth: int):
		evaluations = {}
		for i in range(len(board)):
			game = Connect4()
			game.table = deepcopy(board)
			# evaluations[i] = self._minimax(game, depth, True) 
			if game.play_move(i, 2):
				evaluations[i] = self._minimax(game, depth-1, False)
		print(evaluations)
		highest_score = max(evaluations, key=evaluations.get)
		all_highest_scores = []
		for score in evaluations:
			if score == highest_score:
				all_highest_scores.append(score)
		return choice(all_highest_scores)
		

