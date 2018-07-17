class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = len(s)
        substring = []
        for i in range(1,int(m/2)+1):
            if m % i == 0 and s == s[:i] * (int(m/i)):
                return True
        return False

print(Solution.repeatedSubstringPattern(Solution, "hello"))