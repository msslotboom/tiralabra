from connect4 import Connect4
HEURISTIC_MULTIPLIER = 100
HEURISTIC_WIN_SCORE = 10000


class Heuristic():
    """Heuristic class that gives a score to the game situation.
    Used by the minimax algorithm to give a score to each scenario
    it runs through"""

    def __init__(self) -> None:
        pass

    def calculate_score(self, game: Connect4, depth: int):
        """Gives the score to the game. Higher is better for player 2.
        A win gives a positive or negative HEURISTIC_WIN_SCORE, a sequence
        that is one off four in a row gives the amount of points
        defined in the constant HEURISTIC_MULTIPLIER"""
        if game.calculate_winner():
            row, col = game.last_added
            if game.table[row][col] == 2:
                return HEURISTIC_WIN_SCORE+depth
            return -HEURISTIC_WIN_SCORE-depth
        return self._calculate_heuristic(game)

    def _calculate_heuristic(self, game: Connect4):
        table = game.table
        negative_values_sum = 0
        positive_values_sum = 0
        sequences = self._get_all_sequences(table)
        for sequence in sequences:
            count = self.count_one_off_four_in_a_row(sequence)
            negative_values_sum += count[0]
            positive_values_sum += count[1]
        score = HEURISTIC_MULTIPLIER * \
            (positive_values_sum - negative_values_sum)
        return score

    def _get_all_sequences(self, table):
        """Gets all sequences from the board. 
        This code is divided into different functions per direction,
        that this function calls"""
        all_sequences = []
        for sequence in self._get_horizontal_sequences(table):
            all_sequences.append(sequence)
        for sequence in self._get_vertical_sequences(table):
            all_sequences.append(sequence)
        for sequence in self._get_lowering_diagonal_sequences(table):
            all_sequences.append(sequence)
        for sequence in self._get_rising_diagonal_sequences(table):
            all_sequences.append(sequence)
        return all_sequences

    def _get_horizontal_sequences(self, table):
        all_horizontal_sequences = []
        for row in table:
            all_horizontal_sequences.append(row)
        return all_horizontal_sequences

    def _get_vertical_sequences(self, table):
        all_vertical_rows = []
        for column_index in range(len(table[0])):
            vertical_row = []
            for row_index in range(len(table)):
                vertical_row.append(table[row_index][column_index])
            all_vertical_rows.append(vertical_row)
        return all_vertical_rows

    def _get_lowering_diagonal_sequences(self, table):
        all_lowering_diagonal_sequences = []
        for starting_row_index in range(len(table)-4, -1, -1):
            diagonal_sequence = []
            column_index = 0
            for row_index in range(starting_row_index, len(table)):
                diagonal_sequence.append(table[row_index][column_index])
                column_index += 1
            all_lowering_diagonal_sequences.append(diagonal_sequence)
        for starting_column_index in range(1,  len(table[0])-3):
            diagonal_sequence = []
            row_index = 0
            for column_index in range(starting_column_index, len(table[0])):
                diagonal_sequence.append(table[row_index][column_index])
                row_index += 1
            all_lowering_diagonal_sequences.append(diagonal_sequence)
        return all_lowering_diagonal_sequences

    def _get_rising_diagonal_sequences(self, table):
        all_rising_diagonal_sequences = []
        for starting_column_index in range(len(table[0])-4, -1, -1):
            rising_sequence = []
            row_index = len(table)-1
            for column_index in range(starting_column_index, len(table[0])):
                rising_sequence.append(table[row_index][column_index])
                row_index -= 1
            all_rising_diagonal_sequences.append(rising_sequence)
        for starting_row_index in range(len(table)-2, 2, -1):
            column_index = 0
            rising_sequence = []
            for row_index in range(starting_row_index, -1, -1):
                rising_sequence.append(table[row_index][column_index])
                column_index += 1
            all_rising_diagonal_sequences.append(rising_sequence)
        return all_rising_diagonal_sequences

    def count_one_off_four_in_a_row(self, row: list):
        """Function that counts the scenarios where a player has a sequence
        where if it fills in one empty spot the player gets a four in a row
        and wins. """
        top_counter = {}
        top_counter[1] = 0
        top_counter[2] = 0
        player = -1
        counter = 0
        zero_counter = {}
        zero_counter[1] = 0
        zero_counter[2] = 0
        for item in row:
            if item == 0:
                if player == -1:
                    counter = 1
                else:
                    # If not first zero: remove previous zerocounter from counter,
                    # add one, store new zerocounter for that player,
                    # update other players counter to 1
                    if zero_counter[player] != 0:
                        counter -= zero_counter[player]
                        zero_counter[player] = counter + 1
                        counter += 1
                        if player == 1:
                            zero_counter[2] = 1
                        else:
                            zero_counter[1] = 1

                    # If first zero: zerocounter up for both
                    else:
                        if player == 1:
                            zero_counter[1] = counter + 1
                            zero_counter[2] = 1
                        else:
                            zero_counter[2] = counter + 1
                            zero_counter[1] = 1
                        counter += 1
            elif item == player:
                counter += 1
                if player == 1:
                    zero_counter[2] = 0
                else:
                    zero_counter[1] = 0
            else:
                if player == -1 and counter == 1:
                    counter = 2
                    player = item
                    zero_counter[player] = 1
                else:
                    player = item
                    counter = zero_counter[player] + 1
                if player == 1:
                    zero_counter[2] = 0
                else:
                    zero_counter[1] = 0
            if counter == 4:
                top_counter[player] += 1
        return top_counter[1], top_counter[2]
