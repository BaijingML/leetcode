class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return None
        n = len(nums)
        first = 0
        last = n - 1
        if nums[0] > target:
            return 0
        if nums[n-1] < target:
            return n
        while first <= last:
            mid = int((first + last) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                last = mid - 1
            else:
                first = mid + 1
        return first