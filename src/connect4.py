class Connect4:
    """The class that contains all the game logic and stores the current game situation. The game is run by the gameloop class.

    Attributes:
            table: stores the current game. 0 in the table means empty, 1 means a human player and 2 means the algorithm.
            last_added: stores a tuple (row, column) where row and column are the indexes of the last played move 
    """

    def __init__(self) -> None:
        self.table = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]]

        self.last_added = (0, 0)

    def play_move(self, col: int, player: int) -> bool:
        """Plays a move into the specified column col by the player called player. Returns true if succesfull and false when unsuccessfull. Note that the leftmost column has index 0."""
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
        """Calculates whether the previous move was a winning move. The last played move is saved into self.last_added in the play_move function"""
        row, col = self.last_added
        player = self.table[row][col]
        horizontal_four = self._check_horizontal_winner(row, col, player)
        vertical_four = self._check_vertical_winner(row, col, player)
        diag_1_four = self._check_rising_diag(row, col, player)
        diag_2_four = self._check_lowering_diag(row, col, player)
        if horizontal_four or vertical_four or diag_1_four or diag_2_four:
            return True
        return False

    def board_is_full(self) -> bool:
        """Checks whether the board is full"""
        for item in self.table[0]:
            if item == 0:
                return False
        return True

    def _check_horizontal_winner(self, row: int, col: int, player: int) -> bool:
        """Function called by the calculate_winner function to check whether the previously played move was a winning move by checking if there are four in a row horizontally from the position of the previous move

        Args:
            row: row of the previously played move
            col: column of the previously played move
            player: the player that played the previous move"""
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
        """Function called by the calculate_winner function to check whether the previously played move was a winning move by checking if there are four in a row vertically from the position of the previous move

        Args:
            row: row of the previously played move
            col: column of the previously played move
            player: the player that played the previous move"""
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
        """Function called by the calculate_winner function to check whether the previously played move was a winning move. Checks the vertical that rises when going to the right for four in a row

        Args:
            row: row of the previously played move
            col: column of the previously played move
            player: the player that played the previous move"""
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
        """Function called by the calculate_winner function to check whether the previously played move was a winning move. Checks the vertical that lowers when going to the right for four in a row

        Args:
            row: row of the previously played move
            col: column of the previously played move
            player: the player that played the previous move"""
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
