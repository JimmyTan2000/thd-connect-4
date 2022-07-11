Feature: Player vs AI

  Scenario: Player lose to AI
    Given I start the program
    When I am in the main menu
    And I enter 1 to choose Player vs. AI
    And X chooses 1. column
    And X chooses 7. column
    And X chooses 1. column
    And X chooses 4. column
    And X chooses 7. column
    And X chooses 7. column
    Then Player O wins

  Scenario: Player win to AI
    Given I start the program
    When I am in the main menu
    And I enter 1 to choose Player vs. AI
    And X chooses 3. column
    And X chooses 3. column
    And X chooses 3. column
    And X chooses 4. column
    And X chooses 1. column
    And X chooses 2. column
    And X chooses 5. column
    And X chooses 2. column
    And X chooses 5. column
    And X chooses 5. column
    Then Player X wins