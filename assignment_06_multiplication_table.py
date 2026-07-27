# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_single_table(number):
    #This should print the multiplication table for a single number from 1 to 12.
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        product = number * i
        print(f"{number} x {i} = {product}")

def print_tables_up_to_n(n):
    #This should print multiplication tables for all numbers from 1 to n.
    for number in range(1, n + 1):
        print_single_table(number)
        print("-" * 30)  # Separator line between tables

def main():
    #This is the main function to execute the multiplication table generator.
    choice = input("Do you want a single table or tables up to N? (Enter 'single' or 'up to N'): ").strip().lower()
    
    if choice == 'single':
        number = int(input("Enter a number for its multiplication table: "))
        print_single_table(number)
    elif choice == 'up to n':
        n = int(input("Enter a positive integer N to print tables from 1 to N: "))
        if n <= 0:
            print("Error: N must be a positive integer.")
            return
        print_tables_up_to_n(n)
    else:
        print("Invalid choice. Please enter 'single' or 'up to N'.")

if __name__ == "__main__":
    main()          