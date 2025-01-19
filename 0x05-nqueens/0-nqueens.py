#!/usr/bin/python3
"""N Queens Problem Solver"""
import sys


def print_error_and_exit(message, status_code):
    """Print error message and exit with a status code."""
    print(message)
    exit(status_code)


# Input validation
if len(sys.argv) != 2:
    print_error_and_exit("Usage: nqueens N", 1)

if not sys.argv[1].isdigit():
    print_error_and_exit("N must be a number", 1)

N = int(sys.argv[1])

if N < 4:
    print_error_and_exit("N must be at least 4", 1)


def solve_nqueens(N):
    """Solve the N Queens problem using backtracking."""
    def backtrack(row, columns, diagonals1, diagonals2, board):
        """Recursive helper to explore solutions."""
        if row == N:
            # Add a valid solution
            solutions.append([pos[:] for pos in board])
            return

        for col in range(N):
            if col not in columns and (row + col) not in diagonals1 and (row - col) not in diagonals2:
                # Choose
                board.append([row, col])
                columns.add(col)
                diagonals1.add(row + col)
                diagonals2.add(row - col)

                # Explore
                backtrack(row + 1, columns, diagonals1, diagonals2, board)

                # Un-choose
                board.pop()
                columns.remove(col)
                diagonals1.remove(row + col)
                diagonals2.remove(row - col)

    solutions = []
    backtrack(0, set(), set(), set(), [])
    return solutions


# Generate and print all solutions
solutions = solve_nqueens(N)
for solution in solutions:
    print(solution)
