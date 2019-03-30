class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N
        pre = 0
        post = 1
        result = 0
        for i in range(2, N+1):
            result = pre + post
            pre = post
            post = result
        return result