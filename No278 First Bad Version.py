# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        first = 1
        last = n
        while first <= last:
            mid = int((first + last) / 2)
            if isBadVersion(mid):
                last = mid - 1
            else:
                first = mid + 1
        return first