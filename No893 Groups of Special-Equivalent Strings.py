class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if not A:
            return 0
        return len({''.join(sorted(i[0::2])) + ''.join(sorted(i[1::2])) for i in A})