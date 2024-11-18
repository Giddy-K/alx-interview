#!/usr/bin/python3
"""
Test script for rotate_2d_matrix function
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

def main():
    # Test case 1: 3x3 matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Original matrix:")
    print_matrix(matrix)

    rotate_2d_matrix(matrix)
    print("\nRotated matrix:")
    print_matrix(matrix)

    # Expected output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    # Test case 2: 4x4 matrix
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print("\nOriginal matrix:")
    print_matrix(matrix)

    rotate_2d_matrix(matrix)
    print("\nRotated matrix:")
    print_matrix(matrix)

    # Expected output: [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]

    # Test case 3: 2x2 matrix
    matrix = [
        [1, 2],
        [3, 4]
    ]
    print("\nOriginal matrix:")
    print_matrix(matrix)

    rotate_2d_matrix(matrix)
    print("\nRotated matrix:")
    print_matrix(matrix)

    # Expected output: [[3, 1], [4, 2]]

def print_matrix(matrix):
    """
    Helper function to print a matrix in a readable format
    """
    for row in matrix:
        print(row)

if __name__ == "__main__":
    main()
