# Myself solution

# def flipAndInvertImage(A):
#     m = len(A)
#     n = len(A[0])
#     B = []
#     for i in range(m):
#         B.append(A[i][::-1])
#     for i in range(m):
#         for j in range(n):
#             B[i][j] = 1 - B[i][j]
#     return B

def flipAndInvertImage(A):
    for row in A:
        for i in range((len(row) + 1) / 2):
            row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1   # [i]和[~i]是交换位置
    return A

A = [[1,1,0],[1,0,1],[0,0,0]]
print(flipAndInvertImage(A))