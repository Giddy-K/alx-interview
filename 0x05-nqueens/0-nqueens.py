#!/usr/bin/python3
""" N Queens """
import sys

# Check for correct usage and input validation
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Ensure that N is a positive integer
try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Ensure N is at least 4
if n < 4:
    print("N must be at least 4")
    sys.exit(1)

# Recursive function to find solutions
def queens(n, row=0, columns=[], diag1=[], diag2=[]):
    """Generate valid queen placements for the current row."""
    if row == n:
        # Each solution is represented by the list of positions
        solution = [[i, columns[i]] for i in range(n)]
        yield solution
    else:
        for col in range(n):
            if col not in columns and row + col not in diag1 and row - col not in diag2:
                # Recursively place the next queen
                yield from queens(n, row + 1, columns + [col], diag1 + [row + col], diag2 + [row - col])

# Function to print all solutions
def solve(n):
    """Print all solutions for the n-queens problem."""
    for solution in queens(n):
        print(solution)

# Run the solver
solve(n)
