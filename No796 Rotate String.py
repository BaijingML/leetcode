class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """

        n = len(B)
        if A == '' and B == '':
            return True
        for i in range(1, n):
            if B == A[i:]+A[:i]:
                return True
            else:
                continue
        return False

        # 更快的办法
        # return len(A) == len(B) and B in A + A

if __name__ == '__main__':
    solu = Solution()
    print(solu.rotateString('abcde', 'cdeab'))