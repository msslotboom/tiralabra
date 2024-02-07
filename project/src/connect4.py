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

    def board_is_full(self) -> bool:
        for item in self.table[0]:
            if item == 0:
                return False
        return True
    
    def _check_horizontal_winner(self, row: int, col: int, player: int) -> bool:
        counter = 1
        for i in range(1, 4):
            if row+i == len(self.table):
                break
            if self.table[row+i][col] == player:
                counter += 1
            else:
                break
        for i in range(1, 4):
            if row-i < 0:
                break
            if self.table[row-i][col] == player:
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
            if row+i == len(self.table) or col+i == len(self.table[row]):
                break
            if self.table[row+i][col+i] == player:
                counter += 1
            else:
                break
        for i in range(1, 4):
            if row-i < 0 or col-i < 0:
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
            if row+i == len(self.table) or col-i < 0:
                break
            if self.table[row+i][col-i] == player:
                counter += 1
            else:
                break
        for i in range(1, 4):
            if row-i < 0 or col+i == len(self.table[row-i]):
                break
            if self.table[row-i][col+i] == player:
                counter += 1
            else:
                break
        if counter == 4:
            return True

        return False
