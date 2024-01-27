import random


class Connect4:
    def __init__(self) -> None:
        self.table = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]]

        self.last_added = (0, 0)

        # TODO: does not account for board being full
    def play(self):
        while True:
            for row in self.table:
                print(row)
            move = int(input("Pick which column to play"))
            if move >= len(self.table[0]) or move < 0:
                print("Invalid move!")
                continue
            if not self.play_move(move, 1):
                print("Invalid move!")
                continue
            if self.calculate_winner():
                print("You won!")
                break
            self._play_random_move()
            if self.calculate_winner():
                print("You lost!")
                break

        # TODO: Does not account for board being full
    def _play_random_move(self):
        while True:
            random_move = random.randint(0, len(self.table[0])-1)
            if not self.play_move(random_move, 2):
                continue
            break
	
    def play_move(self, col, player) -> bool:
        if self.table[0][col] != 0:
            return False
        for index in range(len(self.table)):
            if self.table[index][col] == 0:
                continue
            self.table[index-1][col] = player
            self.last_added = (index-1, col)
            return True
        self.table[len(self.table)-1][col] = player
        self.last_added = (len(self.table)-1, col)
        return True
    
    def calculate_winner(self) -> bool:
        row, col = self.last_added
        # Check all directions from new move to see if previous move triggered a win
        player = self.table[row][col]
        horizontal_four = self._check_horizontal_winner(row, col, player)
        vertical_four = self._check_vertical_winner(row, col, player)
        diag_1_four = self._check_rising_diag(row, col, player)
        diag_2_four = self._check_lowering_diag(row, col, player)
        if horizontal_four or vertical_four or diag_1_four or diag_2_four:
            return True
        return False

    def _check_horizontal_winner(self, row: int, col: int, player: int) -> bool:
        counter = 1
        for i in range(1, 4):
            if row+i == len(self.table):
                break
            if self.table[row+i][col] == player:
                print(row+i, col, self.table[row+i][col])
                counter += 1
            else:
                break
        for i in range(1, 4):
            if row-i < 0:
                break
            if self.table[row-i][col] == player:
                print(row-i, col, self.table[row-i][col])
                counter += 1
            else:
                break
        if counter == 4:
            return True
        return False

    def _check_vertical_winner(self, row: int, col: int, player: int) -> bool:
        counter = 1
        for i in range(1, 4):
            if col+i == len(self.table[row]):
                break
            if self.table[row][col+i] == player:
                counter += 1
            else:
                break
        for i in range(1, 4):
            if col-i < 0:
                break
            if self.table[row][col-i] == player:
                counter += 1
            else:
                break
        if counter == 4:
            return True
        return False

    def _check_rising_diag(self, row: int, col: int, player: int) -> bool:
        counter = 1
        for i in range(1, 4):
            if row+i == len(self.table) or col+1 == len(self.table[row+i]):
                break
            if self.table[row+i][col+i] == player:
                counter += 1
            else:
                break
        for i in range(1, 4):
            if row-i < 0 or col-1 < 0:
                break
            if self.table[row-i][col-i] == player:
                counter += 1
            else:
                break
        if counter == 4:
            return True
        return False

    def _check_lowering_diag(self, row: int, col: int, player: int) -> bool:
        counter = 1
        for i in range(1, 4):
            if row+i == len(self.table) or col-1 < 0:
                break
            if self.table[row+i][col-i] == player:
                counter += 1
            else:
                break
        for i in range(1, 4):
            if row-i < 0 or col+1 == len(self.table[row-i]):
                break
            if self.table[row-i][col+i] == player:
                counter += 1
            else:
                break
        if counter == 4:
            return True

        return False
