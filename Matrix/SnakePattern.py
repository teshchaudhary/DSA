def snakePattern(mat):
    for i in range(len(mat)):
        if i % 2 == 0:
            for j in range(len(mat[i])):
                print(mat[i][j], end = " ")
    
        else:
            for j in range(len(mat[i])-1,-1,-1):
                print(mat[i][j], end = " ")
        
        print()

mat = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]]

snakePattern(mat)