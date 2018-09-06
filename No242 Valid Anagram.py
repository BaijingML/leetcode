class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            s_set = set(s)
            s_dict = {}
            t_set = set(t)
            if s_set != t_set:
                return False
            for i in s_set:
                s_dict[i] = s.count(i)
            for j in t_set:
                if s_dict[j] != t.count(j):
                    return False
            return True

if __name__ == '__main__':
    solu = Solution()
    print(solu.isAnagram("aacc","ccac"))