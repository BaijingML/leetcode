class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        pre = 0
        post = 1
        if not nums: return None
        while post <= len(nums) - 1:
            if nums[pre] == nums[post]:
                post += 1
            else:
                pre += 1
                nums[pre] = nums[post]
        return pre + 1

if __name__ == '__main__':
    Solu = Solution()
    print(Solu.removeDuplicates([1,1]))