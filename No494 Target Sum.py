class Solution:
    def findTargetSumWays(self, nums, S):
        result_max = sum(nums)
        result_min = -result_max
        result = [0 for i in range(result_min, result_max + 1)]
        result[result_max+nums[0]], result[result_max-nums[0]] = 1, 1
        print(result)
        for i in nums[1:]:
            for j in range(len(result)):
                result[j] = result[result_max - i] + result[result_max + i]
            print(result)
        print(result)
        return result[S + result_max]

if __name__ == '__main__':
    Solu = Solution()
    print(Solu.findTargetSumWays([1,1,2,1,1], 3))