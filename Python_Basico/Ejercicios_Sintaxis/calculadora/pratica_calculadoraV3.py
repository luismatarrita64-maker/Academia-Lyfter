def sum_function(a, b):
    return a + b

def subtraction_function(a, b):
    return a - b

def multiply_function(a, b):
    return a * b

def divide_function(a, b):
    if b == 0:
        print("Error: cannot divide by zero")
        return a
    return a / b

def menu_calculator():
    actual = 0
    while True:
        print("Actual number:", actual)
        print("Menu")
        print("1. Sum")
        print("2. Subtraction")
        print("3. Multiply")
        print("4. Divide")
        print("5. Delete result")
        print("6. Exit")

        option = input("Select an option: ")
        if not option.isdigit():
            print("Error: the option must be a number")
            continue
        option = int(option)

        if option < 1 or option > 6:
            print("Error: invalid option")
            continue

        if option == 6:
            print("Leaving...")
            break

        if option == 5:
            actual = 0
            print("Result deleted")
            continue

        new = input("Enter the second number: ")
        try:
            new = float(new)
        except ValueError:
            print("Error: enter a valid number")
            continue

        
        if option == 1:
            actual = sum_function(actual,new)
        elif option == 2:
            actual = subtraction_function(actual, new)
        elif option == 3:
            actual = multiply_function(actual, new)
        elif option == 4:
            actual = divide_function(actual, new)

menu_calculator()

