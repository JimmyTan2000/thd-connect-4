from abc import ABC, abstractmethod
import gameboard as gb
from enum import Enum

class PlayerTypeNotKnownError(Exception):
    """
    Raised when the player type is not known.
    """
    pass

class PlayerActionNotKnownError(Exception):
    """
    Raised when the player action is not known.
    """
    pass

class PlayerType(Enum):
    HUMAN = 'human'
    AI = 'ai'

class PlayerAction(Enum):
    MOVE_MADE = 'move_made'
    INGAME_MENU = 'ingame_menu'

class Player(ABC):
    """Represents the player of the game."""

    def __init__(self, token: str, board: gb.Gameboard):
        """
        :param token: The token of the AI. Must be a single character.
        :param board: GameBoard instance that the AI is playing on.
        :raises InvalidTokenError: raised when the length of token is not equal to 1
        """

        if len(token) != 1:
            raise gb.InvalidTokenError('Token must be one character long.')

        self._token = token
        self._board = board
    
    @abstractmethod
    def make_move(self) -> PlayerAction:
        pass

    def is_winner(self) -> bool:
        """
        Checks if the player has won.
        """

        return self._board.check_win(self._token)

    @property
    def token(self):
        """
        Returns the token of the player.
        """
        return self._token