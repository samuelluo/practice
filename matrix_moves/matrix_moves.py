"""
There is an N by M matrix of zeroes. Given N and M, write a function to count 
the number of ways of starting at the top-left corner and getting to the 
bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two 
ways to get to the bottom-right:
Right, then down
Down, then right

Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
"""

# -----------------------------------------------
def matrix_moves(N, M):
    matrix = [[0 for j in range(M)] for i in range(N)]
    matrix[N-1][M-1] = 1
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if i+1 < N:
                matrix[i][j] += matrix[i+1][j]
            if j+1 < M:
                matrix[i][j] += matrix[i][j+1]
    return matrix[0][0]

# -----------------------------------------------
N = 2
M = 2
result = matrix_moves(N, M)
print(result)

N = 5
M = 5
result = matrix_moves(N, M)
print(result)