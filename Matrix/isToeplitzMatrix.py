"""A Toeplitz (or diagonal-constant) matrix is a matrix in which each descending diagonal from left to right is constant, i.e., all elements in a diagonal are the same. Given a rectangular matrix mat, your task is to complete the function isToeplitz which returns true if the matrix is Toeplitz otherwise, it returns false."""

def isToeplitzMatrix(mat):
    m = len(mat)
    n = len(mat[0])
    for i in range(1, m):
        for j in range(1, n):
            if mat[i][j] != mat[i-1][j-1]:
                return False

    return True


mat =  [[6, 7, 8],
       [4, 6, 7],
       [1, 4, 6]]

print(isToeplitzMatrix(mat))