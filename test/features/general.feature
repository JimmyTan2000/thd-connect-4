Feature: General

    Scenario: Choose About
        Given I start the program
        When I am in the main menu
        And I enter 5 to choose About
        Then I see the game description

    Scenario: Choose exit
        Given I start the program
        When I am in the main menu
        And I enter 6 to choose exit
        Then I see goodbye message

    Scenario: Choose Load game
        Given I start the program
        When I am in the main menu
        And I enter 4 to choose Load Game
        Then I see no saved game found message