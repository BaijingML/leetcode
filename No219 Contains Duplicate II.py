class Solution:
    def containsNearbyDuplicate(self, nums,k):
        if not nums or k > len(nums):
            return False
        for i in range(len(nums)-k):
            print(nums[i], nums[i+k])
            if nums[i] == nums[i+k]:
                return True
        return False

if __name__ == '__main__':
    Solu = Solution()
    print(Solu.containsNearbyDuplicate([1,0,1,1], 1))