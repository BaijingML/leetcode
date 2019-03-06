class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A:
            return None
        start = 0
        end = len(A) - 1
        while start < end:
            while A[start] % 2 == 0 and start < end:
                start += 1
            while A[end] % 2 == 1 and start < end:
                end -= 1
            A[start], A[end] = A[end], A[start]
        return A