from behave import when, then
import os


@when("I enter {num} to choose About")
def step_impl(context, num):
    context.proc.expect("Select an option:")
    context.proc.sendline(num)


@when("I enter {num} to choose exit")
def step_impl(context, num):
    context.proc.expect("Select an option:")
    context.proc.sendline(num)


@when("I enter {num} to choose Load Game")
def step_impl(context, num):
    context.saved_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data/save_state.pkl')
    if os.path.exists(context.saved_dir):
        os.remove(context.saved_dir)
    context.proc.expect("Select an option:")
    context.proc.sendline(num)


@when("I am in the main menu")
def step_impl(context):
    context.proc.expect("New game: Player vs. AI")
    context.proc.expect("New game: Player vs. Player")
    context.proc.expect("New game: AI vs. AI")
    context.proc.expect("Load game")
    context.proc.expect("About")
    context.proc.expect("Exit")


@then("I see the game description")
def step_impl(context):
    context.proc.expect("Connect 4 is a game console application.")


@then("I see goodbye message")
def step_impl(context):
    context.proc.expect("Thank you for playing. Goodbye!")


@then("I see no saved game found message")
def step_impl(context):
    context.proc.expect("No saved game found.")


@then("I am in the main menu")
def step_impl(context):
    context.proc.expect("New game: Player vs. AI")
    context.proc.expect("New game: Player vs. Player")
    context.proc.expect("New game: AI vs. AI")
    context.proc.expect("Load game")
    context.proc.expect("About")
    context.proc.expect("Exit")
    context.proc.expect("Select an option:")
