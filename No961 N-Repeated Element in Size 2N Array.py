class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(len(A)):
            if A[i] in A[0:i]:
                return A[i]