import os
from behave import given, when, then
import pexpect

@given("I start the program")
def step_impl(context):
    APP_PATH = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src', 'main.py')
    context.proc = pexpect.spawn(f"python {APP_PATH}", timeout=100)


@when("I enter {num} to choose Player vs. Player")
def step_impl(context, num):
    context.proc.expect("Select an option:")
    context.proc.sendline(num)

@when("{player} chooses {col}. column")
def step_impl(context, player, col):
    context.proc.expect(f"Player {player}:")
    context.proc.sendline(col)

@then("Player {player} wins")
def step_impl(context, player):
    context.proc.expect(f'PLAYER "{player}" WINS!')

@then("Column {col} is full")
def step_impl(context, col): 
    context.proc.expect(f'Column {col} is full.')
    
@then("It's a tie")
def step_impl(context): 
    context.proc.expect("TIE!")

@then("Player is told that column must be between 1 and 7")
def step_impl(context): 
    context.proc.expect("Column must be between 1 and 7.")