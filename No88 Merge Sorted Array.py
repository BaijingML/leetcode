class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return
        while m > 0 and n > 0:
            if nums2[n-1] >= nums1[m-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
        if n > 0:
            nums1[:n] = nums2[:n]


if __name__ == '__main__':
    solu = Solution()
    solu.merge([1,2,10,0,0,0],3,[2,5,6],3)