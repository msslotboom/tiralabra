from copy import deepcopy
from random import choice
from connect4 import Connect4
from heuristic import Heuristic
from math import floor

class Minimax():
    """Minimax algorithm, calculates the best move. 
    It simulates a game where both players play optimally, 
    and then selects the move where it has the biggest advantage"""

    def __init__(self, debug:bool=False) -> None:
        self.heuristic = Heuristic()
        self.organised_moves = []
        self.debug = debug
        if self.debug:
            self.result = []

    def _calculate_heuristic_score(self, game: Connect4, depth: int) -> int:
        """Heuristic function that calls the heuristic class to calculate a heuristic value"""
        return self.heuristic.calculate_score(game, depth)

    def _organise_moves(self, moves_length):
        new_moves_list = []
        index = floor(moves_length/2)
        down = True
        jump = 1
        for i in range(moves_length):
            new_moves_list.append(index)
            if down:
                index -= jump
                down = False
            else:
                index += jump
                down = True
            jump += 1
        return new_moves_list

    def _minimax(self, game: Connect4, depth: int, maximising: bool, alpha: int, beta: int, first_run: bool = True, move: int = -1) -> int:
        """Algorithm that maximises the move of the computer
        and minimises the move of the human player. Note that the heuristic
        gives a negative value when the move is good for the human player, 
        whichs means that it is effectively
        playing the best moves for both player"""
        if first_run:
            self.organised_moves = self._organise_moves(len(game.table[0]))
        if depth == 0 or game.calculate_winner():
            return self._calculate_heuristic_score(game, depth), move
        if maximising:
            value = -100000000000
            for index in self.organised_moves:
                new_game = Connect4()
                new_game.table = deepcopy(game.table)
                if new_game.play_move(index, 2):
                    if first_run:
                        move = index
                    result = self._minimax(
                        new_game, depth-1, False, alpha, beta, False, move)
                    if first_run and self.debug:
                        self.result.append(result)
                    if result[0] > value:
                        value = result[0]
                        best_move = result[1]
                    alpha = max(value, alpha)
                    if beta <= alpha:
                        break
            return value, best_move if first_run else move
        else:
            value = 100000000000
            for index in self.organised_moves:
                new_game = Connect4()
                new_game.table = deepcopy(game.table)
                if new_game.play_move(index, 1):
                    if first_run:
                        move = index
                    result = self._minimax(
                        new_game, depth-1, True, alpha, beta, False, move)
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
        if self.debug:
            self.result = []
        calculation_result = self._minimax(
            game, depth, True, -100000000000, 100000000000)
        best_move = calculation_result[1]
        if self.debug:
            print(sorted(self.result, key = lambda result: result[1]))
        return best_move
