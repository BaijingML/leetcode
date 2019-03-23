class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        post = [1] * n
        res = [1] * n
        if not nums:
            return []
        for i in range(n-1):
            pre[i+1] = nums[i] * pre[i]
            post[n-2-i] = nums[n-1-i] * post[n-1-i]
        for i in range(n):
            res[i] = pre[i] * post[i]
        return res