class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if not A:
            return 0
        # character = [chr(i) for i in range(97,123)]
        # number = {i:x for x, i in enumerate(character)}
        count = 0
        for i in range(len(A[0])):
            for j in range(len(A)-1):
                # if number[A[j][i]] <= number[A[j+1][i]]:
                if A[j][i] <= A[j+1][i]:
                    continue
                else:
                    count += 1
                    break
        return count

if __name__ == '__main__':
    solu = Solution()
    print(solu.minDeletionSize(["abc", "def", "ghi"]))