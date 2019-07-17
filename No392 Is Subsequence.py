class Solution:
    def isSubsequence(self, s, t):
        s_point = 0
        t_point = 0
        m = len(s)
        n = len(t)
        while t_point < n and s_point < m:
            if t[t_point] == s[s_point]:
                s_point += 1
            t_point += 1
        return s_point == m
