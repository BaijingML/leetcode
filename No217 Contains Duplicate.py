class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == []:
            return False
        nums_set = set(nums)
        if len(nums_set) != len(nums):
            return True
        else:
            return False










if __name__ == '__main__':
    solu = Solution()
    print(solu.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))