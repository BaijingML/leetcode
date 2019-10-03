class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return None
        final_max = nums[0]
        cur_max = nums[0]
        for i in range(1, len(nums)):
            if cur_max + nums[i] < nums[i]:
                cur_max = nums[i]
            else:
                cur_max += nums[i]
            if cur_max > final_max:
                final_max = cur_max
        return final_max

if __name__ == '__main__':
    Solu = Solution()
    print(Solu.maxSubArray([-2,1,-3,4,-1,2,1,-5,4,6]))