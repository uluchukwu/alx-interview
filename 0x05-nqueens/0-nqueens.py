#!/usr/bin/python3
import sys


def print_usage():
    print("Usage: nqueens N")
    sys.exit(1)


def print_error(message):
    print(message)
    sys.exit(1)


def is_safe(board, row, col):
    """Check if a queen can be placed on board[row][col]."""
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, solutions):
    """Use backtracking to find all solutions."""
    if col >= len(board):
        # All queens are placed, store the solution
        solutions.append([[i, board[i].index(1)] for i in range(len(board))])
        return

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, solutions)
            board[i][col] = 0  # Backtrack


def solve_nqueens(n):
    """Initialize the board and solve the N queens problem."""
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, solutions)
    return solutions


def main():
    """Main entry point for the script."""
    if len(sys.argv) != 2:
        print_usage()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print_error("N must be a number")

    if n < 4:
        print_error("N must be at least 4")

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
