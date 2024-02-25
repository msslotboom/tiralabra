from minimax import Minimax
from connect4 import Connect4
from gameloop import GameLoop
game = Connect4()
gameloop = GameLoop(game)
gameloop.run()

# game.table = [[0, 0, 0, 0, 0, 0, 0],
#               [0, 0, 0, 0, 0, 0, 0],
#               [1, 0, 0, 1, 0, 2, 0],
#               [0, 1, 1, 0, 2, 0, 0],
#               [0, 1, 1, 2, 1, 0, 0],
#               [1, 1, 2, 1, 0, 0, 0]]

# game.table = [[0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0],
# [2, 0, 0, 0, 0, 0, 0],
# [2, 0, 0, 0, 0, 0, 0],
# [2, 0, 0, 0, 0, 0, 0],
# [1, 1, 1, 2, 0, 0, 0]]
# game.last_added = (5,2)
# algo = Minimax()
# algo.calculate_move(game.table, 5)
# # algo = Minimax()
