class Solution:
    def maxProfit(self, prices):
        length = len(prices)
        if length==0:
            return 0
        temp = prices[length-1]
        profit = 0
        for i in range(length-1,-1,-1):
            temp = max(temp, prices[i])
            if temp - prices[i] > profit:
                profit = temp - prices[i]
        return profit

if __name__ == '__main__':
    Solu = Solution()
    print(Solu.maxProfit([7,1,4,3,1]))