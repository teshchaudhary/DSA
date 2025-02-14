def boundaryTraversal(mat):
    rows = len(mat)
    columns = len(mat[0])

    if rows == 1:
        print(mat[0], end=' ')

    elif columns == 1:
        for i in range(rows):
            print(mat[i][0], end=' ')
    else:
        i, j = 0, 0
        
        while j < columns:
            print(mat[i][j], end = " ")
            j += 1

        i += 1
        j -= 1

        while i < rows:
            print(mat[i][j], end = " ")
            i += 1
        
        i -= 1
        j -= 1

        while j > -1:
            print(mat[i][j], end = " ")
            j -= 1
        
        j += 1
        i -= 1
        while i > 0:
            print(mat[i][j], end = " ")
            i -= 1
        
mat = [
["00", "01", "02", "03"],
["10", "11", "12", "13"],
["20", "21", "22", "23"],
["30", "31", "32", "33"]
]

boundaryTraversal(mat)