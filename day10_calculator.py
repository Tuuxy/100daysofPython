import day10_art


def add(a,b):
    """Adds two numbers together."""
    return a+b

def subtract(a,b):
    """Subtract two numbers together."""
    return a-b

def multiply(a,b):
    """Multiply two numbers together."""
    return a*b

def divide(a,b):
    """Divide two numbers together."""
    if b == 0:
        print("Sorry, you can't divide by zero, try again.")
        return None
    return a/b

def calculus(a,b,operation):
    operations = {
        "+":add,
        "-":subtract,
        "*":multiply,   
        "/":divide,
    }
    return operations[operation](a,b)

def get_number(prompt):
    """Validate user input to receive an integer"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input, please enter a valid number.")

def get_operation():
    """Validate user input to receive a valid operation"""
    valid = ["+","-","*","/"]
    while True:
        operation = input("+\n-\n*\n/\nPick an operation: ")
        if operation in valid:
            return operation
        print("Invalid operation, please choose from '+' '-' '*' or '/'.")

def main():
    print(day10_art.logo)
    a = get_number("What is the first number?: ")

    while True:
        operation = get_operation()
        b = get_number("What's the next number?: ")
        result = calculus(a,b,operation)

        if result is None:
            continue

        print(f"{a} {operation} {b} = {result}")
        keep_going = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if keep_going == "y":
            a = result
        else:
            main()

if __name__ == "__main__":
    main()