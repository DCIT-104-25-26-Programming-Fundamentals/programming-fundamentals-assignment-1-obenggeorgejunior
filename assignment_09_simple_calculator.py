#===============================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

 

# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# Topic: Console-Based Simple Calculator
# =============================================================================


def add(num1, num2):
    #this shouldReturns the sum of two numbers.
    return num1 + num2


def subtract(num1, num2):
    #this should Returns the difference of two numbers.
    return num1 - num2


def multiply(num1, num2):
    #this should Returns the product of two numbers.
    return num1 * num2


def divide(num1, num2):
    #thi sReturns the quotient rounded to 2 decimal places, or an error string if zero.
    if num2 == 0:
        return "Error: Cannot divide by zero."
    return round(num1 / num2, 2)


def modulus(num1, num2):
    #Returns the remainder of division, or an error string if zero.
    if num2 == 0:
        return "Error: Cannot perform modulus by zero."
    return num1 % num2


def exponentiate(num1, num2):
    #Returns num1 raised to the power of num2.
    return num1 ** num2


def get_number_input(prompt):
    #Helper function to ensure valid numeric inputs without crashing.
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def main():
    #Main program loop and menu driver.
    while True:
        print("\n============================")
        print("      SIMPLE CALCULATOR     ")
        print("============================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Quit")

        choice = input("Select an operation (1-7): ").strip()

        # Exit condition
        if choice == "7":
            print("Goodbye!")
            break

        # Check for valid operation choices
        if choice in ("1", "2", "3", "4", "5", "6"):
            num1 = get_number_input("Enter first number : ")
            num2 = get_number_input("Enter second number: ")

            if choice == "1":
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")

            elif choice == "2":
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")

            elif choice == "3":
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")

            elif choice == "4":
                result = divide(num1, num2)
                if isinstance(result, str):  # Error message returned
                    print(result)
                else:
                    print(f"Result: {num1} / {num2} = {result}")

            elif choice == "5":
                result = modulus(num1, num2)
                if isinstance(result, str):  # Error message returned
                    print(result)
                else:
                    print(f"Result: {num1} % {num2} = {result}")

            elif choice == "6":
                result = exponentiate(num1, num2)
                print(f"Result: {num1} ** {num2} = {result}")

        else:
            print("Invalid choice! Please select an option between 1 and 7.")


# Run the calculator application
if __name__ == "__main__":
    main()
