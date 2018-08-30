class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        s_dict = Counter(s)
        for i in t:
            if i not in s_dict:
                return i
            else:
                s_dict[i] -= 1
                if s_dict[i] == -1:
                    return i
    def findTheDifference2(self, s, t):
        st=set(t)
        for i in st:
            if i not in s:return i
            if t.count(i)>s.count(i):
                return i


if __name__ == '__main__':

    solu = Solution()
    print(solu.findTheDifference('a', 'aa'))