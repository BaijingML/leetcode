class Solution:
    def threeSumClosest(self, nums, target):
        closest = float('inf')
        res = 0
        if not nums:
            return []
        n = len(nums)
        nums.sort()
        for i in range(n):
            j = i+1
            k = n-1
            while j < k:
                m = nums[i] + nums[j] + nums[k]
                print(m)
                if m == target:
                    return m
                elif m < target:
                    if abs(target - m) < closest:
                        closest = abs(target - m)
                        res = m
                    j += 1
                else:
                    if abs(target - m) < closest:
                        closest = abs(target - m)
                        res = m
                        print(11111111111)
                    k -= 1

        return res
if __name__ == '__main__':
    Solu = Solution()
    print(Solu.threeSumClosest([1,1,1,1], 0))