#!/usr/bin/python3

"""sys module inport"""
import sys

"""we are looking if number of argument are correct"""
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

""" we are looking if N is the positive integer"""
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

""" looking  if N is least 4"""
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

""" The function to check if a position is safe"""
def safe(board, row, col):
    """ look at the row"""
    for k in range(col):
        if board[row][k] == 1:
            return False
    """Check the upper diagonal"""
    for k, a in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[k][a] == 1:
            return False
    """ the lower diagonal"""
    for k, a in zip(range(row, N, 1), range(col, -1, -1)):
        if board[k][a] == 1:
            return False
    """Return true if no conflict"""
    return True

"""function to solve the problem recursively"""
def nqueens(board, col):
    if col == N:
        solution = []
        for k in range(N):
            for a in range(N):
                if board[k][a] == 1:
                    solution.append([k, a])
        print(solution)
        return
    """all rows in the current column"""
    for k in range(N):
        if safe(board, k, col):
            board[k][col] = 1
            nqueens(board, col + 1)
            board[k][col] = 0

board = [[0 for k in range(N)] for a in range(N)]

# Call the solver function
nqueens(board, 0) 
