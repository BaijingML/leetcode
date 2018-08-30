class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = int(len(nums) / 2)
        nums_set = set(nums)
        for i in nums_set:
            if nums.count(i) > n:
                return i

if __name__ == '__main__':
    solu = Solution()
    print(solu.majorityElement([3,2,3]))