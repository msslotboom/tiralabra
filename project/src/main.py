from minimax import Minimax
from connect4 import Connect4
from gameloop import GameLoop
game = Connect4()
gameloop = GameLoop(game)
# gameloop.run()

game.table = [[0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [1, 0, 0, 1, 0, 2, 0],
              [0, 1, 1, 0, 2, 0, 0],
              [0, 1, 1, 2, 1, 0, 0],
              [1, 1, 2, 1, 0, 0, 0]]

algo = Minimax()
val = algo._count_one_off_four_diag_lowering(game)
