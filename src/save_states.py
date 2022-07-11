import pickle
import os

from gameboard import Gameboard
from player import Player


class SaveStateNotFoundError(Exception):
    """ Raised when the save state file is not found. """
    pass


class SaveState:
    """
    Class for saving and loading game states.
    """

    def __init__(self):
        self._DEFAULT_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'data')
        self._DEFAULT_FILE = os.path.join(self._DEFAULT_ROOT, 'save_state.pkl')

        # create save path if it doesn't exist
        if not os.path.exists(self._DEFAULT_ROOT) or not os.path.isdir(self._DEFAULT_ROOT):
            os.mkdir(self._DEFAULT_ROOT)

    def save(self, board: Gameboard, curr_player_index: int, players: list[Player]):
        """
        Save board and players to save file in the default location. (default location: '../data/save_state.pkl')

        :param board: Gameboard instance to save.
        :param curr_player_index: Index of the current player.
        :param players: List of Player instances to save.
        """
        output_data = (board, curr_player_index, players)

        with open(self._DEFAULT_FILE, 'wb') as f:
            pickle.dump(output_data, f)

    def load(self) -> tuple[Gameboard, int, list[Player]]:
        """
        Load board and players from save file in the default location. (default location: '../data/save_state.pkl')

        :return: Tuple of Gameboard instance and list of Player instances.
        :raises SaveStateNotFoundError: If the save file is not found.
        """
        if not os.path.exists(self._DEFAULT_FILE):
            raise SaveStateNotFoundError('Save file not found.')

        with open(self._DEFAULT_FILE, 'rb') as f:
            input_data = pickle.load(f)

        return input_data
