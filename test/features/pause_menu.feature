Feature: Pause Menu

    Scenario: Open the pause menu in a player vs. AI match
        Given I start the program
        When I am in the main menu
        And I enter 1 to choose Player vs. AI
        And I enter m to open the pause menu
        Then I am in the pause menu


    Scenario: Open the pause menu in a player vs. AI match then resume the game
        Given I start the program
        When I am in the main menu
        And I enter 1 to choose Player vs. AI
        And I enter m to open the pause menu
        And I am in the pause menu
        And I enter 1 to resume the game
        Then The game resumes

    Scenario: Open the pause menu in a player vs. AI match then save and exit to main menu
        Given I start the program
        When I am in the main menu
        And I enter 1 to choose Player vs. AI
        And I enter m to open the pause menu
        And I am in the pause menu
        And I enter 2 to save and exit to main menu
        Then I am in the main menu

    Scenario: Open the pause menu in a player vs. AI match then exit to main menu
        Given I start the program
        When I am in the main menu
        And I enter 1 to choose Player vs. AI
        And I enter m to open the pause menu
        And I am in the pause menu
        And I enter 3 to exit to main menu
        Then I am in the main menu

    Scenario: Open the pause menu in a player vs. AI match and save and exit to main menu, then load the saved file
        Given I start the program
        When I am in the main menu
        And I enter 1 to choose Player vs. AI
        And I enter m to open the pause menu
        And I am in the pause menu
        And I enter 2 to save and exit to main menu
        And I am in the main menu
        And I enter 4 to load the saved file
        Then I pick up the game state from last save

    Scenario: Open the pause menu in a player vs. AI match then, save and exit to main menu, then exit the game
        Given I start the program
        When I am in the main menu
        And I enter 1 to choose Player vs. AI
        And I enter m to open the pause menu
        And I am in the pause menu
        And I enter 2 to save and exit to main menu
        And I am in the main menu
        And I enter 6 to choose exit
        Then I see goodbye message