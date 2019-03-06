class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])
        print(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        return result

if __name__ == '__main__':
    solu = Solution()
    print(solu.findDisappearedNumbers([4,3,2,7,8,2,3,1]))