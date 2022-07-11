from behave import when, then


@when("I enter {str} to open the pause menu")
def step_impl(context, str):
    context.proc.expect("Player X:")
    context.proc.sendline(str)

@when("I am in the pause menu")
def step_impl(context):
    context.proc.expect("Resume")
    context.proc.expect("Save & Exit to main menu")
    context.proc.expect("Exit to main menu")

@when("I enter {num} to resume the game")
def step_impl(context, num):
    context.proc.expect("Select an option:")
    context.proc.sendline(num)

@when("I enter {num} to save and exit to main menu")
def step_impl(context, num):
    context.proc.expect("Select an option:")
    context.proc.sendline(num)

@when("I enter {num} to exit to main menu")
def step_impl(context, num):
    context.proc.expect("Select an option:")
    context.proc.sendline(num)

@when("I enter {num} to load the saved file")
def step_impl(context, num):
    context.proc.expect("Select an option:")
    context.proc.sendline(num)

@then("Player {player} chooses {col}. column")
def step_impl(context, player, col):
    context.proc.expect(f"Player {player}:")
    context.proc.sendline(col)

@then("The game resumes")
def step_impl(context):
    context.proc.expect(f"Player X:")

@then("I pick up the game state from last save")
def step_impl(context):
    context.proc.expect(f"Player X:")

@then("I am in the pause menu")
def step_impl(context):
    context.proc.expect("Resume")
    context.proc.expect("Save & Exit to main menu")
    context.proc.expect("Exit to main menu")
    context.proc.expect("Select an option:")
