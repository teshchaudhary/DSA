# Naive
def transpose(mat):
    m = len(mat)

    temp = [[0 for i in range(m)] for i in range(m)]
    for i in range(m):
        for j in range(m):
            temp[i][j] = mat[j][i]
    
    for i in temp:
        print(i)

# Better
def Transpose(mat):
    m = len(mat)

    for i in range(m):
        for j in range(i+1, m):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    
    for i in mat:
        print(i)

mat = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]]

transpose(mat)
Transpose(mat)