class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """

        if ops == []:
            return m*n
        else:
            a = ops[0][1]
            b = ops[0][0]
            for i in range(len(ops)):
                a = min(ops[i][1], a)
                b = min(ops[i][0], b)
            return a*b