# Naive
# The last column becomes the first row
# The second last column becomes the second row

def rotate(mat):
    N = len(mat)
    temp = [[0]*N for i in range(N)]

    for i in range(N):
        for j in range(N):
            temp[N-j-1][i] = mat[i][j]
            
    for i in range(N):
        for j in range(N):
            print(temp[i][j], end = " ")
        print()

# Efficient Approach
# Tranpose the matrix and then reverse the order of the columns

def Rotate(mat):
    N = len(mat)
    for i in range(N):
        for j in range(i+1, N):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    
    for i in range(N):
        low = 0 
        high = N-1
        while(low < high):
            mat[low][i], mat[high][i] = mat[high][i], mat[low][i]
            low += 1 
            high -= 1 
            
    #print rotated matrix
    for i in range(N):
        for j in range(N):
            print(mat[i][j], end = " ")
        print()
        
mat = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]]

rotate(mat)