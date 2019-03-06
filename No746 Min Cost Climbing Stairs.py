class Solution:
    def minCostClimbingStairs(self, cost: 'List[int]') -> 'int':
        if not cost: return 0
        for i in range(2, len(cost)):
            cost[i] = min(cost[i-1], cost[i-2]) + cost[i]
        return min(cost[i-1], cost[i])

if __name__ == '__main__':
    Solu = Solution()
    print(Solu.minCostClimbingStairs([0,0,0,1]))