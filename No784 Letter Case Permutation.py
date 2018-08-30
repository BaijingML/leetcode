class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ans = []
        def dsf(S, pos, str):
            if pos == len(S):
                ans.append(str)
                return ans
            else:
                if S[pos].isalpha():
                    dsf(S, pos+1, str + S[pos].upper())
                    dsf(S, pos+1, str + S[pos].lower())
                else:
                    dsf(S, pos+1, str + S[pos])

        dsf(S, 0, '')
        return ans

if __name__ == '__main__':
    solu = Solution()
    print(solu.letterCasePermutation("a1b2"))

