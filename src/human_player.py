from player import Player, PlayerAction
from gameboard import Gameboard, ColumnOutOfRangeError, ColumnIsFullError


class HumanPlayer(Player):
    """Represents the human player of the game."""

    def __init__(self, token: str, board: Gameboard):
        """
        :param token: The token of the AI. Must be a single character.
        :param board: GameBoard instance that the AI is playing on.
        """
        super().__init__(token, board)

    def make_move(self):
        """
        Makes human player move. The human player selects a column and drops a token in that column.
        """
        success = False
        while not success:
            try:
                inp = input(f'Player {self._token}: ')

                if inp.isdigit():
                    self._board.drop_token(int(inp), self._token)
                elif inp == 'm':
                    return PlayerAction.INGAME_MENU
                else:
                    raise ValueError('Invalid input.')

                success = True

            except ValueError as vex:
                print(vex)
            except ColumnOutOfRangeError as crex:
                print(crex)
            except ColumnIsFullError as cfex:
                print(cfex)

        return PlayerAction.MOVE_MADE
