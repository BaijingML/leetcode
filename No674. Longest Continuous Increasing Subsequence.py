class Solution:
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0
        n = len(nums)
        start = 0
        end = 0
        max_len = 0
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                end += 1
            else:
                max_len = max(max_len, end-start+1)
                start = end = i
        print(end, start)
        max_len = max(max_len, end - start + 1)
        return max_len
if __name__ == '__main__':
    Solu = Solution()
    print(Solu.findLengthOfLCIS([1,3,5,7]))
