import collections


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_dict = dict(collections.Counter(s))
        for i in range(len(s)):
            if s_dict[s[i]] == 1:
                return i
        return -1

print(Solution.firstUniqChar(Solution, "loveleetcode"))