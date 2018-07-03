def peakIndexInMountainArray(A):
    a = A[0]
    b = 0
    for i in range(1, len(A)):
        if A[i] > a:
            a = A[i]
            b = i
        else:
            pass
    return b

