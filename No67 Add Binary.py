class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c = 0
        l = max(len(a), len(b))
        b = b.zfill(l)
        a = a.zfill(l)
        sum = ''
        for i in range(l, -1, -1):
