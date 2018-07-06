def matrixReshape(nums, r, c):
    if len(nums) * len(nums[0]) != r * c:
        return nums
    else:
        L = []
        for i in nums:
            L.extend(i)
        s = []
        print(L)
        for j in range(int(len(L)/c)):
            s.append(L[j*c:(j+1)*c])
    return s
print(matrixReshape([[1,2],[3,4]], 1, 4))
