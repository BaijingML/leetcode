class Solution:
    def missingNumber(self, nums: 'List[int]') -> 'int':
        num_sum = 0
        if not nums: return None
        for i in nums:
            num_sum += i
        n = len(nums)
        return int(n * (n + 1) / 2 - num_sum)