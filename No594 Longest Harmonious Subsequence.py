class Solution:
    def findLHS(self, nums):
        if not nums:
            return 0
        max_len = 0
        temp = {}
        for i in nums:
            if i in temp:
                temp[i] += 1
            else:
                temp[i] = 1
        for i in temp:
            if temp.get(i+1):
                max_len = max(max_len, temp[i] + temp[i+1])
        return max_len
if __name__ == "__main__":
    Solu = Solution()
    print(Solu.findLHS([1,1,1,1,1]))