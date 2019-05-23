class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # return list(zip(*A))
        m = len(A)
        n = len(A[0])
        B = [[0] * m] * n
        for i in range(m):
            for j in range(n):
                B[j][i] = A[i][j]
                print(i, j, B)
        return B

if __name__ == '__main__':
    Solu = Solution()
    print(Solu.transpose([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))