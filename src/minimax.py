from copy import deepcopy
from random import choice
from connect4 import Connect4
from heuristic import Heuristic

class Minimax():
    """Minimax algorithm, calculates the best move. 
    It simulates a game where both players play optimally, 
    and then selects the move where it has the biggest advantage"""

    def __init__(self) -> None:
        self.heuristic = Heuristic()

    def _calculate_heuristic_score(self, game: Connect4) -> int:
        """Heuristic function that calls the heuristic class to calculate a heuristic value"""
        return self.heuristic.calculate_score(game)

    def _minimax(self, game: Connect4, depth: int, maximising: bool, alpha:int, beta:int, first_run:bool=True, move:int=-1) -> int:
        """Algorithm that maximises the move of the computer
        and minimises the move of the human player. Note that the heuristic
        gives a negative value when the move is good for the human player, 
        whichs means that it is effectively
        playing the best moves for both player"""
        if depth == 0 or game.calculate_winner():
            return self._calculate_heuristic_score(game), move
        if maximising:
            value = -100000000000
            for i in range(len(game.table)):
                new_game = Connect4()
                new_game.table = deepcopy(game.table)
                if new_game.play_move(i, 2):
                    if first_run:
                        move = i
                    result = self._minimax(new_game, depth-1, False, alpha, beta, False, move)
                    if result[0] > value:
                        value = result[0]
                        best_move = result[1]
                    alpha = max(value, alpha)
                    if beta <= alpha:
                        break
            return value, best_move if first_run else move
        else:
            value = 100000000000
            for i in range(len(game.table)):
                new_game = Connect4()
                new_game.table = deepcopy(game.table)
                if new_game.play_move(i, 1):
                    if first_run:
                        move = i
                    result = self._minimax(new_game, depth-1, True, alpha, beta, False, move)
                    if result[0] < value:
                        value = result[0]
                        best_move = result[1]
                    beta = min(beta, value)
                    if beta <= alpha:
                        break
            return value, best_move if first_run else move

    def calculate_move(self, game: Connect4, depth: int) -> int:
        """Calculates the best move by calling the minimax algorithm. 
        It gives all its possible moves to the minimax algorithm, 
        returns the index of the best move"""
        calculation_result = self._minimax(game, depth, True, -100000000000, 100000000000)
        print(calculation_result)
        best_move = calculation_result[1]
        return best_move

    def _select_highest_random_score(self, evaluations: list) -> int:
        """Function called by calculate move,
        to make sure that if there are multiple optimal moves,
        the selection of the optimal move is random"""
        highest_score = max(evaluations, key=evaluations.get)
        all_highest_scores = []
        for score in evaluations:
            if score == highest_score:
                all_highest_scores.append(score)
        return choice(all_highest_scores)
