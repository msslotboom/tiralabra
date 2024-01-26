from connect4 import Connect4

game = Connect4()

game.table = [[0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0],
				[1, 0, 0, 0, 0, 0, 0],
				[1, 0, 0, 0, 0, 0, 0],
				[1, 0, 0, 0, 0, 0, 0],
				[1, 0, 0, 0, 0, 0, 0]]

game.play_move(1, 2)
print(game.table)
# game.last_added = (2,0)
# result = game.calculate_winner()
# # print(result)

# game.table = [[0, 0, 0, 0, 0, 0, 0],
# 				[0, 0, 0, 0, 0, 0, 0],
# 				[0, 0, 0, 0, 0, 0, 0],
# 				[0, 0, 0, 0, 0, 0, 0],
# 				[0, 0, 0, 0, 0, 0, 0],
# 				[1, 1, 1, 1, 0, 0, 0]]

# game.last_added = (5,0)
# result = game.calculate_winner()
# print(result)

# game.table = [[0, 0, 0, 0, 0, 0, 0],
# 				[0, 0, 0, 0, 0, 0, 0],
# 				[0, 0, 0, 1, 0, 0, 0],
# 				[0, 0, 1, 0, 0, 0, 0],
# 				[0, 1, 0, 0, 0, 0, 0],
# 				[1, 0, 1, 1, 0, 0, 0]]

# game.last_added = (5,0)
# result = game.calculate_winner()
# print(result)


# game.table = [[0, 0, 0, 0, 0, 0, 0],
# 				[0, 0, 0, 0, 0, 0, 0],
# 				[0, 1, 0, 1, 0, 0, 0],
# 				[0, 0, 1, 0, 0, 0, 0],
# 				[0, 1, 0, 1, 0, 0, 0],
# 				[1, 0, 1, 1, 1, 0, 0]]

# game.last_added = (2,1)
# result = game.calculate_winner()
# print(result)