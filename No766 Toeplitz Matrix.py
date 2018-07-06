def isToeplitzMatrix(matrix):
    a = len(matrix)
    b = len(matrix[0])
    if b == 1 or a == 1:
        return True
    else:
        flag = True
        for i in range(1, a):
            for j in range(1, b):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    flag = False
                    break
                else:
                    continue
    return flag
print(isToeplitzMatrix([[11,74,0,93],[40,11,74,7]]))