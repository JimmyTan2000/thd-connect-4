from __future__ import annotations  # this is needed to typehint inside of the same class
from gameboard import Gameboard
from human_player import HumanPlayer
from player import Player, PlayerType, PlayerTypeNotKnownError, PlayerAction, PlayerActionNotKnownError
from ai_player import AIPlayer
from human_player import HumanPlayer
from save_states import SaveState
from util import clear_screen
from termcolor import colored, cprint


class Game():

    @classmethod
    def from_save_file(cls) -> Game:
        """
        constructs a game from a save file.

        :return: Game instance
        :raises SaveStateNotFoundError: raised when the save file does not exist.
        """
        board, curr_player_index, players = SaveState().load()
        return cls(board, curr_player_index, *players)

    @classmethod
    def from_new_game(cls, type_player1: PlayerType, type_player2: PlayerType) -> Game:
        """
        Constructs a new game.

        :param player1: PlayerType enum value for player 1.
        :param player2: PlayerType enum value for player 2.
        :return: Game instance
        """
        board = Gameboard()
        player1 = Game._create_player(type_player1, 'X', 'O', board)
        player2 = Game._create_player(type_player2, 'O', 'X', board)
        return Game(board, 0, player1, player2)

    def __init__(self, board: Gameboard, curr_player_index: int, player1: Player, player2: Player):
        """
        DO NOT CALL THIS CONTRUCTOR DIRECTLY. IT IS MEANT TO BE PRIVATE.
        The game class will be initialized by a from_* method.

        :param board: Gameboard instance
        :param curr_player_index: index of the current player
        :param player1: Player instance
        :param player2: Player instance
        """
        self._board = board
        self._players = [player1, player2]
        self._running = True
        self._curr_player_index = curr_player_index  # index of the current player
        self._rules = (
            colored('Enter an integer between 1 to 7.', 'white'),
            colored('Whoever stacks 4 tokens next to each other,', 'white'),
            colored('either horizontally, vertically or diagonally wins.', 'white'),
            colored('Press "m" to show the ingame menu.', 'white'),
            colored('{}\n\n'.format('\n'.join(
                [f'Player {i+1}: {player._token}' for i, player in enumerate(self._players)])), 'white')
        )

    @staticmethod
    def _create_player(type_player, own_token: str, enemy_token: str, board: Gameboard) -> Player:
        """
        Constucts a player instance based on the player type.

        :param type_player: PlayerType enum value.
        :param own_token: token of the player.
        :param enemy_token: token of the enemy player.
        :param board: Gameboard instance.
        :return: Player instance.
        :raises PlayerTypeNotKnownError: raised when the player type is not known.
        """
        # fmt: off
        match type_player:
            case PlayerType.HUMAN: return HumanPlayer(own_token, board)
            case PlayerType.AI: return AIPlayer(board, own_token, enemy_token)
            case _: raise PlayerTypeNotKnownError
        # fmt: on

    def run(self):
        """
        Main game loop.
        """

        clear_screen()
        for rule in self._rules:
            print(rule)

        while self._running:

            for p in self._players[self._curr_player_index:] + self._players[:self._curr_player_index]:
                self._move(p)
                self._curr_player_index = (self._players.index(p) + 1) % len(self._players)

                if self._running == False:
                    break

    def _move(self, player):
        move_running = True

        while move_running:
            self._board.display()
            action = player.make_move()
            clear_screen()

            if player.is_winner():
                self._gameover(f'PLAYER "{player._token}" WINS!')
                return

            if self._board.check_tie():
                self._gameover('TIE!')
                return

            if action == PlayerAction.INGAME_MENU:
                move_running = self._ingame_menu()
                clear_screen()
            else:
                move_running = False

    def _gameover(self, msg: str):
        clear_screen()
        cprint("""
   _____                         ____                 _ 
  / ____|                       / __ \               | |
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __| |
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__| |
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |  |_|
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|  (_)
            """, 'blue')
        cprint(f'\n\n{msg}\n', 'cyan')
        self._gameover_screen()
        clear_screen()

    def _ingame_menu(self) -> bool:
        """
        :return: True if the game should continue, False if it should end.
        """

        options = [
            colored('[1] ', 'yellow') + colored('Resume', 'white'),
            colored('[2] ', 'yellow') + colored('Save & Exit to main menu', 'white'),
            colored('[3] ', 'yellow') + colored('Exit to main menu', 'white'),
        ]

        while True:
            clear_screen()
            cprint("""
  _____                     
 |  __ \                    
 | |__) |_ _ _   _ ___  ___ 
 |  ___/ _` | | | / __|/ _ \\
 | |  | (_| | |_| \__ \  __/
 |_|   \__,_|\__,_|___/\___|
                            

            """, 'blue')

            for option in options:
                print(option)

            inp = input('\nSelect an option: ')

            # fmt: off
            match inp:
                case '1': return True
                case '2': SaveState().save(self._board, self._curr_player_index, self._players); self._running = False; return False
                case '3': self._running = False; return False
                case _: print('Invalid option. Please try again.')
            # fmt: on

    def _gameover_screen(self):
        """
        Displays the game over screen.
        """
        options = [
            colored('[1] ', 'yellow') + colored('Try again', 'white'),
            colored('[2] ', 'yellow') + colored('Exit to main menu', 'white'),
        ]

        while True:

            for el in options:
                print(el)

            inp = input('\nSelect an option: ')

            # fmt: off
            match inp:
                case '1': self._board.reset_board(); return
                case '2': self._running = False; return
                case _: clear_screen(); cprint('Invalid option. Please try again.', 'red')
            # fmt: on
