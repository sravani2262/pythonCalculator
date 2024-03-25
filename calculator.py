def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def exponentiate(x, y):
    return x ** y

def calculator():
    print("Welcome to the Simple Calculator with Advanced Features!")
    print("Available operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Quit")

    while True:
        choice = input("Enter operation number (1-6): ")
        if choice in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue
            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '5':
                print("Result:", exponentiate(num1, num2))

        elif choice == '6':
            print("Thank you for using the calculator.")
            break
        else:
            print("Invalid input! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    calculator()
