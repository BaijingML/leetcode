class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        bigger = True
        for i in range(1, len(A)):
            if A[i-1] < A[i]:
                bigger = False
                break
        smaller = True
        for i in range(1, len(A)):
            if A[i-1] > A[i]:
                smaller = False
                break
        return bigger or smaller
if __name__ == '__main__':
    solu = Solution()
    print(solu.isMonotonic([1,2,2,3]))