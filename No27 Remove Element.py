class Solution:
    def removeElement(self, nums: 'List[int]', val: 'int') -> 'int':
        if not nums: return 0
        point = 0
        while point < len(nums):
            if nums[point] == val:
                nums.pop(point)
            else:
                point += 1
        return len(nums)

if __name__ == '__main__':
    Solu = Solution()
    print(Solu.removeElement([0,1,2,2,3,0,4,2], 2))