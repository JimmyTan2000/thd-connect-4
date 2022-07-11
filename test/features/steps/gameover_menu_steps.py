from behave import when, then

@when("Player {player} wins")
def step_impl(context, player):
    context.proc.expect(f'PLAYER "{player}" WINS!')

@when("chooses {num} to exit to main menu")
def step_impl(context, num):
    context.proc.expect("Select an option:")
    context.proc.sendline(num)

@when("chooses {num} to try again")
def step_impl(context, num):
    context.proc.expect("Select an option:")
    context.proc.sendline(num)

@then("I am in a new game")
def step_impl(context):
    context.proc.expect("Player O:")

