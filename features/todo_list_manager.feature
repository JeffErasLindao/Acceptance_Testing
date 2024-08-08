Feature: To-Do List Management

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user lists all tasks
    Then the output should contain:
      Tasks:
      - Buy groceries
      - Pay bills

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Task          | Status  |
      | Buy groceries | Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user clears the to-do list
    Then the to-do list should be empty

  # Escenarios adicionales:
  Scenario: Add a task with priority
    Given the to-do list is empty
    When the user adds a task "Finish homework" with priority "High"
    Then the to-do list should contain "Finish homework" with priority "High"

  Scenario: List only completed tasks
    Given the to-do list contains tasks:
      | Task          | Status    |
      | Buy groceries | Completed |
      | Pay bills     | Pending   |
    When the user lists completed tasks
    Then the output should contain:
      Tasks:
      - Buy groceries