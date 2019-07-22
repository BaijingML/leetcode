class Solution:
    def topKFrequent(self, nums, k):
        from collections import defaultdict
        n = len(nums)
        countdict = defaultdict(int)
        for i in nums:
            countdict[i] += 1
        print(countdict)
        temp = [[] for i in range(n+1)]
        for p in countdict:
            print(p,temp, type(p))
            temp[countdict[p]].append(p)
        ans = []
        for p in range(n, 0, -1):
            ans.extend(temp[p])
        return ans[:k]


if __name__ == '__main__':
    Solu = Solution()
    print(Solu.topKFrequent([1,2,3,4,5,6,7,8,9,9], 1))