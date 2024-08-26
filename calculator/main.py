from helpers import (
    ask_for_next_action,
    calculate,
)


def main():
    # List of operations. It can have numbers and aritmethic operations,
    # when an item is "=" it should stop and perform the operations
    operations = []

    action = input(
        'Select your next action, you can put numbers, operations or "=" to see the result: '
    )
    operations = ask_for_next_action(action, ["number", "operation"], operations)

    while len(operations) > 0 and operations[-1] != "=":
        if "=" in operations:
            raise Exception("Something went wrong")

        action = input(
            'Select your next action, you can put numbers, operations or "=" to see the result: '
        )
        operations = ask_for_next_action(action, ["number", "operation"], operations)

    operations.pop()

    print("The result is:", calculate(operations))


main()
