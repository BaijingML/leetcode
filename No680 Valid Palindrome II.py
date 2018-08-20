class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        L = len(s)
        j = 1
        s = list(s)
        for i in range(int(L/2)):
            print(i)
            if s[i] == s[L-1-i]:
                continue
            elif s[i] != s[L-1-i]:
                if s[i] == s[L-1-i-j] and j == 1:
                    s.pop(L-1-i)
                    j = 0
                    print(s)
                elif s[i+j] == s[L-1-i] and j == 1:
                    s.pop(i)
                    j = 0
                    print(s)
                else:
                    return False
        return True
print(Solution.validPalindrome(Solution, "eedede"))