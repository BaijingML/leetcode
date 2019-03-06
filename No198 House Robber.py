class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        pre_sum = nums[0]
        current_sum = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = current_sum
            current_sum = max(pre_sum + nums[i], temp)
            pre_sum = temp
        return current_sum