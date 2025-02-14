def spiralTraversal(mat):
    top = 0
    left = 0
    bottom = len(mat) - 1
    right = len(mat[0]) - 1

    while top <= bottom and left <= right:
        # Top row
        for i in range(left, right+1):
            print(mat[top][i], end = " ")

        top += 1

        # Right Column
        for i in range(top, bottom - 1):
            print(mat[top][i], end = " ")
        
        # Bottom Row
        for i in range(right, left-1, -1):
            print(mat[bottom][i], end = " ")
        
        # 