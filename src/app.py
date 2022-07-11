from game import Game
from player import PlayerType
from save_states import SaveStateNotFoundError
from util import clear_screen

from termcolor import colored, cprint


class App:

    def run(self):
        """
        Displays the main menu.
        """

        # create ascii art that says connect 4
        title = colored("""
#########################################################################
#     ____     _____                            _     _  _    __   __   #
#    / __ \   / ____|                          | |   | || |   \ \ / /   #
#   | |  | | | |     ___  _ __  _ __   ___  ___| |_  | || |_   \ V /    #
#   | |  | | | |    / _ \| '_ \| '_ \ / _ \/ __| __| |__   _|   > <     #
#   | |__| | | |___| (_) | | | | | | |  __/ (__| |_     | |    / . \    #
#    \____/   \_____\___/|_| |_|_| |_|\___|\___|\__|    |_|   /_/ \_\\   #
#                                                                       #
#########################################################################

""", 'blue')

        options = [
            colored('[1] ', 'yellow') + colored('New game: Player vs. AI', 'white'),
            colored('[2] ', 'yellow') + colored('New game: Player vs. Player', 'white'),
            colored('[3] ', 'yellow') + colored('New game: AI vs. AI', 'white'),
            colored('[4] ', 'yellow') + colored('Load game', 'white'),
            colored('[5] ', 'yellow') + colored('About', 'white'),
            colored('[6] ', 'yellow') + colored('Exit', 'white'),
        ]

        clear_screen()
        running = True
        while running:
            print(title)
            for option in options:
                print(option)

            option = input('\nSelect an option: ')

            # fmt: off
            match option:
                case '1': self._start_new_game(PlayerType.HUMAN, PlayerType.AI)
                case '2': self._start_new_game(PlayerType.HUMAN, PlayerType.HUMAN)
                case '3': self._start_new_game(PlayerType.AI, PlayerType.AI)
                case '4': self._load_game()
                case '5': clear_screen(); self._about()
                case '6': running = False; print("Thank you for playing. Goodbye!")
                case _: clear_screen(); print('Invalid option. Please try again.')
            # fmt: on

    def _about(self):
        """
        Display the game description.
        """
        cprint("Connect 4 is a game console application.", 'white')
        print(' ')

    def _start_new_game(self, type_player1: PlayerType, type_player2: PlayerType):
        """
        Starts a new game.
        """
        game = Game.from_new_game(type_player1, type_player2)
        game.run()

    def _load_game(self):
        """
        Loads a saved game.
        """
        try:
            game = Game.from_save_file()
            game.run()
        except SaveStateNotFoundError:
            clear_screen()
            cprint('No saved game found.\n', 'red')
            return
