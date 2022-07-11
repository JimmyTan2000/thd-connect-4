Feature: Player vs Player

  Scenario: Player X wins vertically
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
    Then Player X wins

  Scenario: Player O wins horizontally
    Given I start the program
    When I am in the main menu
    And I enter 2 to choose Player vs. Player
    And X chooses 1. column
    And O chooses 2. column
    And X chooses 2. column
    And O chooses 3. column
    And X chooses 3. column
    And O chooses 4. column
    And X chooses 4. column
    And O chooses 5. column
    Then Player O wins

  Scenario: Player X wins diagonally (positive slope)
    Given I start the program
    When I am in the main menu
    And I enter 2 to choose Player vs. Player
    And X chooses 1. column
    And O chooses 2. column
    And X chooses 2. column
    And O chooses 3. column
    And X chooses 3. column
    And O chooses 4. column
    And X chooses 3. column
    And O chooses 4. column
    And X chooses 3. column
    And O chooses 4. column
    And X chooses 3. column
    Then Player X wins

  Scenario: Player O wins diagonally (negative slope)
    Given I start the program
    When I am in the main menu
    And I enter 2 to choose Player vs. Player
    And X chooses 1. column
    And O chooses 4. column
    And X chooses 3. column
    And O chooses 3. column
    And X chooses 2. column
    And O chooses 2. column
    And X chooses 1. column
    And O chooses 2. column
    And X chooses 1. column
    And O chooses 1. column
    Then Player O wins

  Scenario: Column is Full
    Given I start the program
    When I am in the main menu
    And I enter 2 to choose Player vs. Player
    And X chooses 1. column
    And O chooses 1. column
    And X chooses 1. column
    And O chooses 1. column
    And X chooses 1. column
    And O chooses 1. column
    And X chooses 1. column
    Then Column 1 is full

  Scenario: Draw
    Given I start the program
    When I am in the main menu
    And I enter 2 to choose Player vs. Player
    And X chooses 1. column
    And O chooses 2. column
    And X chooses 1. column
    And O chooses 2. column
    And X chooses 1. column
    And O chooses 2. column
    And X chooses 3. column
    And O chooses 4. column
    And X chooses 3. column
    And O chooses 4. column
    And X chooses 3. column
    And O chooses 4. column
    And X chooses 5. column
    And O chooses 6. column
    And X chooses 5. column
    And O chooses 6. column
    And X chooses 5. column
    And O chooses 6. column
    And X chooses 2. column
    And O chooses 1. column
    And X chooses 4. column
    And O chooses 3. column
    And X chooses 6. column
    And O chooses 5. column
    And X chooses 7. column
    And O chooses 7. column
    And X chooses 7. column
    And O chooses 7. column
    And X chooses 4. column
    And O chooses 3. column
    And X chooses 2. column
    And O chooses 1. column
    And X chooses 5. column
    And O chooses 6. column
    And X chooses 7. column
    And O chooses 1. column
    And X chooses 2. column
    And O chooses 3. column
    And X chooses 5. column
    And O chooses 4. column
    And X chooses 7. column
    And O chooses 6. column
    Then It's a tie

  Scenario: Column out of range
    Given I start the program
    When I am in the main menu
    And I enter 2 to choose Player vs. Player
    And X chooses 8. column
    Then Player is told that column must be between 1 and 7
