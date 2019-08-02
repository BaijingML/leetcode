class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        n = len(nums)
        if nums[n - 1] < target or nums[0] > target:
            return [-1, -1]
        if n == 1 and nums[0] == target:
            return [0, 0]
        def expand(nums, index):
            left = index
            while left >= 1:
                if nums[left-1] == target:
                    left -= 1
                    continue
                else:
                    break
            right = index
            while right <= n-2:
                if nums[right+1] == target:
                    right += 1
                    continue
                else:
                    break
            return [left, right]
        if target == nums[n-1]:
            return expand(nums, n-1)
        if target == nums[0]:
            return expand(nums, 0)
        first = 0
        last = n - 1
        while first <= last:
            mid = int((first + last) / 2)
            if nums[mid] == target:
                return expand(nums, mid)
            elif nums[mid] > target:
                last = mid - 1
            else:
                first = mid + 1
        return [-1, -1] 