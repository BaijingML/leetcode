class Solution:
    def subsets(self, nums):
        result = [[]]
        for i in nums:
            result.append(i)
        for i in range(len(nums)):
