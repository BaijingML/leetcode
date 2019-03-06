class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A = sorted(A)
        for i in range(len(A)-1, 1, -1):
            if (A[i] - A[i-1] >= A[i-2]):
                continue
            else:
                return A[i]+A[i-1]+A[i-2]
        return 0
if __name__ == '__main__':
    solu = Solution()
    print(solu.largestPerimeter([3,6,2,3]))