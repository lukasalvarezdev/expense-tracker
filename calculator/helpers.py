def is_number(val):
    try:
        float(val)
        return True
    except ValueError:
        return False


def is_operation(val):
    return val in ["+", "-", "*", "/"]


def should_get_result(val):
    return val == "="


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y


def do(result, number, operation):
    if operation == "+":
        return add(result, number)
    elif operation == "-":
        return subtract(result, number)
    elif operation == "*":
        return multiply(result, number)
    elif operation == "/":
        return divide(result, number)
    else:
        raise Exception("Invalid operation")


def calculate(operations):
    result = 0

    for index, value in enumerate(operations):
        if is_number(value):
            previous_value = operations[index - 1]

            if index == 0:
                result = value
                continue

            if not is_operation(previous_value):
                continue

            result = do(result, value, previous_value)
        elif is_operation(value):
            continue
    return result


def ask_for_next_action(action, avaliable_actions, operations):
    if is_number(action):
        if "number" in avaliable_actions:
            number = float(action)
            operations.append(number)
        else:
            raise Exception("Only avaliable actions are", avaliable_actions)
    elif is_operation(action):
        if "operation" in avaliable_actions:
            operations.append(action)
        else:
            raise Exception("Only avaliable actions are", avaliable_actions)
    elif should_get_result(action):
        operations.append("=")

    return operations
