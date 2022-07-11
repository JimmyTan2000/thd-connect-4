import math
from gameboard import Gameboard, ColumnIsFullError  
from player import Player, PlayerAction
import copy
import time


class AIPlayer(Player):
    """Represents the AI player of the game."""

    def __init__(self, board: Gameboard, own_token: str, enemy_token: str):
        """
        :param token: The token of the AI. Must be a single character.
        :param board: GameBoard instance that the AI is playing on.
        :param player: The player that the AI is playing against.
        """
        super().__init__(own_token, board)
        self._enemy_token = enemy_token

    def make_move(self) -> PlayerAction:
        """
        Makes AI move. The AI selects a column and drops a token in that column.
        """
        success = False

        while not success:
            try:
                start = time.perf_counter()
                col = self._minimax(self._board, 4, True)[0]
                self._board.drop_token(col+1, self._token)

                success = True
                end = time.perf_counter()
                time.sleep(max(0, 1.0 - (end - start)))

            except ColumnIsFullError as cfex:
                print(cfex)
                
        return PlayerAction.MOVE_MADE


    def _evaluate_window(self, window, token):
        score = 0
        opp_token = self._enemy_token
        if token == self._enemy_token:
            opp_token = self._token

        if window.count(token) == 4:
            score += 100
        elif window.count(token) == 3 and window.count(self._board.empty_token) == 1:
            score += 5
        elif window.count(token) == 2 and window.count(self._board.empty_token) == 2:
            score += 1

        if window.count(opp_token) == 3 and window.count(self._board.empty_token) == 1:
            score -= 4

        return score

    def _score_position(self, board, token):
        window_length = 4
        score = 0

        # Score center column
        center_array = board[self._board.column_count//2]
        center_count = center_array.count(token)
        score += center_count * 3

        # Score Horizontal
        for r in range(self._board.row_count):
            row_array = [board[c][r] for c in range(self._board.column_count)]
            for c in range(self._board.column_count-3):
                window = row_array[c:c+window_length]
                score += self._evaluate_window(window, token)

        # Score Vertical
        for c in range(self._board.column_count):
            col_array = board[c]
            for r in range(self._board.row_count - 3):
                window = col_array[r:r+window_length]
                score += self._evaluate_window(window, token)

        # Score positive sloped diagonal
        for r in range(self._board.row_count-3):
            for c in range(self._board.column_count-3):
                window = [board[c+i][r+i] for i in range(window_length)]
                score += self._evaluate_window(window, token)

        # Score negative sloped diagonal
        for r in range(self._board.row_count-3):
            for c in range(self._board.column_count-3):
                window = [board[c+i][r+3-i] for i in range(window_length)]
                score += self._evaluate_window(window, token)

        return score

    def _is_game_over(self, board):
        """
        Check the conditions in which the game will terminate
        """
        score = 0
        if board.check_win(self._token):
            score = math.inf
        elif board.check_win(self._enemy_token):
            score = - math.inf

        return board.check_win(self._enemy_token) or board.check_win(self._token) \
            or board.check_tie(), score

    def _minimax(self, board, depth, maximizing_player):
        """
        Backtracking algorithm that is used in decision making and game theory to find the optimal 
        move for the AI

        :param board: GameBoard instance that the players are playing on.
        :param depth: Current depth in game tree.
        :param maximizing_player: The player, who tries to get the highest score possible, in this case, the AI.
        :return: a tuple of column and score
        """
        open_columns = board.get_open_columns()
        is_game_over, score = self._is_game_over(board)

        if is_game_over:
            return None, score

        if depth == 0:
            return None, self._score_position(board, self._token)

        if maximizing_player:
            value = -math.inf
            column = open_columns[0]
            for col in open_columns:
                b_copy = copy.deepcopy(board)
                b_copy.drop_token(col+1, self._token)
                new_score = self._minimax(b_copy, depth-1, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
            return column, value

        else:  # Minimizing player
            value = math.inf
            column = open_columns[0]
            for col in open_columns:
                b_copy = copy.deepcopy(board)
                b_copy.drop_token(col+1, self._enemy_token)
                new_score = self._minimax(b_copy, depth-1, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
            return column, value
