# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols):
    #This function reads a matrix of size rows x cols from user input.
    matrix = []
    for i in range(rows):
        while True:
            try:
                row = list(map(int, input(f"Enter row {i + 1}: ").split()))
                if len(row) != cols:
                    raise ValueError(f"Row must have exactly {cols} values.")
                matrix.append(row)
                break
            except ValueError as e:
                print(e)
    return matrix

def print_matrix(matrix):
    #This should print a matrix in a neat, aligned grid format.
    for row in matrix:
        print(" ".join(f"{val:>5}" for val in row))

def transpose_matrix(matrix):
    #This should return the transpose of a given matrix.
    if not matrix:
        return []
    rows, cols = len(matrix), len(matrix[0])
    transposed = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed       

def add_matrices(matrix_a, matrix_b):
    #This should return the element-wise sum of two matrices.
    if not matrix_a or not matrix_b:
        return []
    rows, cols = len(matrix_a), len(matrix_a[0])
    if len(matrix_b) != rows or len(matrix_b[0]) != cols:
        raise ValueError("Matrices must be of the same size for addition.")
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return result

def multiply_matrices(matrix_a, matrix_b):
    #This should return the product of two matrices.
    if not matrix_a or not matrix_b:
        return []
    rows_a, cols_a = len(matrix_a), len(matrix_a[0])
    rows_b, cols_b = len(matrix_b), len(matrix_b[0])
    if cols_a != rows_b:
        raise ValueError("Number of columns in A must equal number of rows in B for multiplication.")
    result = [[0] * cols_b for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result   

def main():
    #This is the main function to perform matrix operations based on user choice.
    print("Matrix Operations Program")
    print("1. Transpose a Matrix")
    print("2. Add Two Matrices")
    print("3. Multiply Two Matrices")
    choice = input("Choose an operation (1-3): ")

    if choice == '1':
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        matrix = read_matrix(rows, cols)
        print("\nOriginal Matrix:")
        print_matrix(matrix)
        transposed = transpose_matrix(matrix)
        print("\nTransposed Matrix:")
        print_matrix(transposed)

    elif choice == '2':
        rows = int(input("Enter number of rows for both matrices: "))
        cols = int(input("Enter number of columns for both matrices: "))
        print("Matrix A:")
        matrix_a = read_matrix(rows, cols)
        print("Matrix B:")
        matrix_b = read_matrix(rows, cols)
        result = add_matrices(matrix_a, matrix_b)
        print("\nResultant Matrix (A + B):")
        print_matrix(result)

    elif choice == '3':
        rows_a = int(input("Enter number of rows for Matrix A: "))
        cols_a = int(input("Enter number of columns for Matrix A: "))
        matrix_a = read_matrix(rows_a, cols_a)
        
        rows_b = int(input("Enter number of rows for Matrix B: "))
        cols_b = int(input("Enter number of columns for Matrix B: "))
        
        if cols_a != rows_b:
            print("Error: Number of columns in A must equal number of rows in B for multiplication.")
            return
        
        matrix_b = read_matrix(rows_b, cols_b)
        
        result = multiply_matrices(matrix_a, matrix_b)
        print("\nResultant Matrix (A x B):")
        print_matrix(result)

    else:
        print("Invalid choice. Please select 1, 2, or 3.")  

        if __name__ == "__main__":
            main()  