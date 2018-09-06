class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        return list(set(nums1) & set(nums2))

if __name__ == '__main__':
    solu = Solution()
    print(solu.intersection([4,9,5], [9,4,9,8,4]))