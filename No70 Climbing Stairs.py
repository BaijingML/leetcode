class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        pre = 1
        post = 2
        for i in range(3, n + 1):
            result = pre + post
            pre = post
            post = result
        return result
if __name__ == '__main__':
    solu = Solution()
    print(solu.climbStairs(3))