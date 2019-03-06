class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        price_min = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < price_min:
                price_min = prices[i]
                continue
            if prices[i] - price_min > profit:
                profit = prices[i] - price_min
            else:
                continue
        return profit


if __name__ == '__main__':
    Solu = Solution()
    print(Solu.maxProfit([9, 11, 8, 5, 7, 12, 16, 14]))