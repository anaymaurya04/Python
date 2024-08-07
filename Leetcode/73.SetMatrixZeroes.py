def setMatrixZeros(matrix):
    row = len(matrix)
    col = len(matrix[0])
    if row == 0:
        return
    rowZero = False
    for i in range(row):
        for j in range(col):
            if matrix[i][j]==0:
                matrix[0][j] = 0
                if i>0:
                    matrix[i][0] = 0
                else:
                    rowZero = True
    for i in range(1,row):
        for j in range(1,col):
            if matrix[0][i] == 0 or matrix [i][0] == 0:
                matrix[i][j]=0
    if matrix[0][0] == 0:
        for i in range(row):
            matrix[i] = 0
    if rowZero is True:
        for j in range(col):
            matrix[j] = 0
