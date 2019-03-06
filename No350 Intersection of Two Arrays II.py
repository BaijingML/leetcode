class Solution(object):
    '''
    这是使用了内置的字典，这样虽然能够简化代码，但方法不够优雅
    '''
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        num = dict()
        for i in nums1:
            if i in num:
                num[i] += 1
            else:
                num[i] = 1
        res = []
        for i in nums2:
            if i in num and num[i] > 0:
                num[i] -= 1
                res.append(i)
        return res
    # 这是先排序，再使用两个指针分别计数
    def insertect1(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        p1 = p2 = 0
        res = []
        while True:
            try:
                if nums1[p1] == nums2[p2]:
                    res.append(nums1[p1])
                    p1 += 1
                    p2 += 1
                else:
                    if nums1[p1] > nums2[p2]:
                        p2 += 1
                    else:
                        p1 += 1
            except:
                return res
if __name__ == '__main__':
    Solu = Solution()
    print(Solu.insertect1([1,2,2,1], [2]))