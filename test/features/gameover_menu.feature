Feature: Game Over Menu

    Scenario: Try again
        Given I start the program
        When I am in the main menu
        And I enter 2 to choose Player vs. Player
        And X chooses 1. column
        And O chooses 1. column
        And X chooses 2. column
        And O chooses 2. column
        And X chooses 3. column
        And O chooses 3. column
        And X chooses 4. column
        And Player X wins
        And chooses 1 to try again
        Then I am in a new game

    Scenario: Exit to main Menu
        Given I start the program
        When I am in the main menu
        And I enter 2 to choose Player vs. Player
        And X chooses 1. column
        And O chooses 2. column
        And X chooses 1. column
        And O chooses 2. column
        And X chooses 1. column
        And O chooses 2. column
        And X chooses 1. column
        And Player X wins
        And chooses 2 to exit to main menu
        Then I am in the main menu

