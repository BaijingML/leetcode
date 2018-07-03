def arrayPairSum(nums):
    nums.sort()
    return sum(nums[::2])

print(arrayPairSum([1,4,3,2]))