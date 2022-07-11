from termcolor import colored


class ColumnIsFullError(Exception):
    """Raised when the token is placed in a fulled column."""
    pass


class ColumnOutOfRangeError(Exception):
    """Raised when the token is not placed in a column that is out of range ."""
    pass


class InvalidTokenError(Exception):
    """Raised when the token is not a single character long."""
    pass


class Gameboard:
    """This class creates a gameboard"""

    def __init__(self):

        self._row_count = 6
        self._col_count = 7
        self._empty_token = ' '

        # structure: [width*Column]
        self._board = [[self._empty_token for _ in range(self._row_count)] for _ in range(self._col_count)]

    def __getitem__(self, key):
        return self._board[key]

    def display(self):
        """
        Display the board.
        """
        # reorder board to resemble a normal y,x coordinate system. x=0 at the left, y=0 at the bottom.
        print_board = list(reversed([[self._board[j][i] for j in range(self._col_count)] for i in range(self._row_count)]))

        padding = '  '
        column_splitter = colored('  |  ', 'yellow')
        column_spacer = colored('---|--', 'yellow')
        row_splitter = f'{column_spacer}{colored("-", "yellow") * (self._col_count*5 + len(padding)*2)}'

        print(f'{" "*6}{column_splitter.join([colored(str(i+1), "green") for i in range(self._col_count)])}{padding}')
        for row in range(self._row_count):
            print(row_splitter)
            print(f' {colored(chr(65+row), "green")} {colored("|", "yellow")}  {column_splitter.join([colored(t, "magenta" if t == "X" else "cyan") for t in print_board[row]])}')

        print(row_splitter)

    def drop_token(self, column: int, token: str):
        """
        Drop token to the column selected by the player.
        """
        if len(token) != 1:
            raise InvalidTokenError('Token must be one character long.')

        if not (1 <= column <= self._col_count):
            raise ColumnOutOfRangeError(
                f'Column must be between 1 and {self._col_count}.')

        if self._board[column - 1][-1] != self._empty_token:
            raise ColumnIsFullError(f'Column {column} is full.')

        # drop token in appropriate slot
        for i, el in enumerate(self._board[column - 1]):  # el is the row
            if el == self._empty_token:
                self._board[column - 1][i] = token
                break

    def can_drop_token(self, col):
        """
        Check if the column is not completely filled.
        """
        return self._board[col][-1] == self._empty_token

    def get_open_columns(self):
        """
        Get a list of columns that are not completely filled in.
        """
        open_columns = []
        for col in range(self.column_count):
            if self.can_drop_token(col):
                open_columns.append(col)
        return open_columns

    def reset_board(self):
        """
        Clear all the tokens from the board when the game restarts.
        """
        self._board = [[self._empty_token for _ in range(self._row_count)] for _ in range(self._col_count)]

    @property
    def column_count(self):
        """
        Returns the number of columns of the board.
        """
        return self._col_count

    @property
    def row_count(self):
        """
        Returns the number of rows of the board.
        """
        return self._row_count

    @property
    def empty_token(self):
        """
        Returns the empty token of the board.
        """
        return self._empty_token

    def check_win(self, token) -> bool:
        """
        Checks if the player has won.
        """

        return self._check_vertical(token) or self._check_horizontal(token) or \
            self._check_diagonal_bltr(token) or self._check_diagonal_brtl(token)

    def check_tie(self) -> bool:
        """
        Checks if the board is full.
        """
        for col in self._board:
            if self._empty_token in col:
                return False

        return True

    def _check_vertical(self, token) -> bool:
        """
        Checks for 4 ajacent tokens vertically.
        """
        for col in self._board:
            for r in range(self._row_count - 3):
                if col[r:r + 4] == [token] * 4:
                    return True

        return False

    def _check_horizontal(self, token) -> bool:
        """
        Checks for 4 ajacent tokens horizontally.
        """
        for c in range(self._col_count - 3):
            for r in range(self._row_count):
                row = [self._board[c + k][r] for k in range(4)]
                if row == [token] * 4:
                    return True

        return False

    def _check_diagonal_bltr(self, token) -> bool:
        """
        Checks for 4 ajacent tokens diagonally from bottom left to top right.
        """
        for c in range(self._col_count - 3):
            for r in range(self._row_count - 3):
                row = [self._board[c + k][r + k] for k in range(4)]
                if row == [token] * 4:
                    return True

        return False

    def _check_diagonal_brtl(self, token) -> bool:
        """
        Checks for 4 ajacent tokens diagonally from bottom right to top left.
        """
        for c in range(self._col_count - 1, 2, -1):
            for r in range(self._row_count - 3):
                row = [self._board[c - k][r + k] for k in range(4)]
                if row == [token] * 4:
                    return True

        return False
