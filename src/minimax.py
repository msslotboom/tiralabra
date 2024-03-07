from copy import deepcopy
from random import choice
from connect4 import Connect4
from heuristic import Heuristic
from math import floor
import time


class Minimax():
    """Minimax algorithm, calculates the best move. 
    It simulates a game where both players play optimally, 
    and then selects the move where it has the biggest advantage"""

    def __init__(self, debug: bool = False) -> None:
        self.heuristic = Heuristic()
        self.debug = debug
        if self.debug:
            self.result = []
        self.time_deepening = False
        self._stored_results = {}
        self.overtime = False

    def _store_result(self, game: Connect4, score: int):
        key = ""
        for row in game.table:
            for item in row:
                key += str(item)
        self._stored_results[key] = score

    def _get_stored_result(self, game: Connect4):
        key = ""
        for row in game.table:
            for item in row:
                key += str(item)
        if key in self._stored_results:
            return self._stored_results[key]
        return False
    
    def _calculate_heuristic_score(self, game: Connect4, depth: int) -> int:
        """Heuristic function that calls the heuristic class to calculate a heuristic value"""
        return self.heuristic.calculate_score(game, depth)

    def _organise_base_moves(self, game:Connect4):
        new_moves_list = []
        moves_length = len(game.table[0])
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
    
    def _order_next_moves(self, game:Connect4, moves: list, maximising: bool):
        if maximising:
            player = 2
        else:
            player = 1
        stored_results_next_moves = []
        for move in moves:
            new_game = Connect4()
            new_game.table = deepcopy(game.table)
            new_game.play_move(move, player)
            stored_result = self._get_stored_result(new_game)
            if stored_result is not False:
                stored_results_next_moves.append((stored_result, move))
        moves_copy = moves.copy()
        moves_order_to_return = []
        sorted_stored_results = sorted(stored_results_next_moves, key=lambda x: x[0])
        for result in sorted_stored_results:
            moves_order_to_return.append(result[1])
            moves_copy.remove(result[1])
        for move in moves_copy:
            moves_order_to_return.append(move)
        return moves_order_to_return

    def _time_check(self):
        if not self.time_deepening:
            return False
        if time.time() - self.start_time > self.time_limit:
            return True
        return False

    def _minimax(self, game: Connect4, depth: int, maximising: bool, alpha: int, beta: int, first_run: bool = True, move: int = -1) -> int:
        """Algorithm that maximises the move of the computer
        and minimises the move of the human player. Note that the heuristic
        gives a negative value when the move is good for the human player, 
        whichs means that it is effectively
        playing the best moves for both player"""
        if self._time_check():
            return -1
        if first_run:
            self.organised_moves = self._organise_base_moves(game)
        if depth == 0 or game.calculate_winner():
            return self._calculate_heuristic_score(game, depth), move
        if maximising:
            value = -100000000000
            organised_next_moves = self._order_next_moves(game, self.organised_moves, maximising)
            for index in organised_next_moves:
                new_game = Connect4()
                new_game.table = deepcopy(game.table)
                if new_game.play_move(index, 2):
                    if first_run:
                        move = index
                    result = self._minimax(
                        new_game, depth-1, False, alpha, beta, False, move)
                    if result != -1:
                        self._store_result(new_game, result[0])
                    if result == -1:
                        break
                    if first_run and self.debug:
                        self.result.append(result)
                    if result[0] > value:
                        value = result[0]
                        best_move = result[1]
                    alpha = max(value, alpha)
                    if beta <= alpha:
                        break
            if value == -100000000000:
                return -1
            return value, best_move if first_run else move
        else:
            value = 100000000000
            organised_next_moves = self._order_next_moves(game, self.organised_moves, maximising)
            for index in organised_next_moves:
                new_game = Connect4()
                new_game.table = deepcopy(game.table)
                if new_game.play_move(index, 1):
                    if first_run:
                        move = index
                    result = self._minimax(
                        new_game, depth-1, True, alpha, beta, False, move)
                    if result != -1:
                        self._store_result(new_game, result[0])
                    if result == -1:
                        break
                    if result[0] < value:
                        value = result[0]
                        best_move = result[1]
                    beta = min(beta, value)
                    if beta <= alpha:
                        break
            if value == 100000000000:
                return -1
            return value, best_move if first_run else move

    def calculate_move_iterative_deepening(self, game: Connect4, time_limit: int):
        depth = 1
        self.start_time = time.time()
        calculation_result = -1
        self.time_limit = time_limit
        self.time_deepening = True
        while time.time() - self.start_time < time_limit:
            self.result = []
            new_calculation_result = self._minimax(
                game, depth, True, -100000000000, 100000000000)
            print(self.result)
            if new_calculation_result == -1 or self.overtime:
                break
            depth += 1
            calculation_result = new_calculation_result
        if self.debug:
            print(sorted(self.result, key=lambda result: result[1]))
            print("Saved heuristic calculations:",
                  self.heuristic.get_saved_calculations())
            print("time:", time.time()-self.start_time)
            print("Depth:", depth)
        return calculation_result[1]

    def calculate_move(self, game: Connect4, depth: int) -> int:
        """Calculates the best move by calling the minimax algorithm. 
        It gives all its possible moves to the minimax algorithm, 
        returns the index of the best move"""
        self.heuristic = Heuristic()
        calculation_result = self._minimax(
            game, depth, True, -100000000000, 100000000000)
        best_move = calculation_result[1]
        if self.debug:
            print(sorted(self.result, key=lambda result: result[1]))
            print("Saved heuristic calculations:",
                  self.heuristic.get_saved_calculations())
        return best_move
