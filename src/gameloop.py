from minimax import Minimax
from connect4 import Connect4


class GameLoop():
    """
    Runs the game and allows for the communication of the algorithm and the human player with the game

    Attributes:
            game: stores the class of the game being played"""

    def __init__(self, game: Connect4) -> None:
        self.game = game

    def run(self):
        while True:
            if self.game.board_is_full():
                print("Draw!")
                break
            for row in self.game.table:
                print(row)
            move = int(input("Pick which column to play: "))
            if move >= len(self.game.table[0]) or move < 0:
                print("Invalid move!")
                continue
            if not self.game.play_move(move, 1):
                print("Invalid move!")
                continue
            if self.game.calculate_winner():
                print("You won!")
                break
            algo = Minimax()
            best_move = algo.calculate_move(self.game.table, 6)
            self.game.play_move(best_move, 2)
            if self.game.calculate_winner():
                print("You lost!")
                for row in self.game.table:
                    print(row)
                break
