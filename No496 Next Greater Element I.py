def nextGreaterElement(nums1, nums2):
    a = []
    pos = dict(map(reversed, enumerate(nums2)))
    for i in range(len(nums1)):
        index = pos[nums1[i]]
        for j in range(index, len(nums2)):
            if nums1[i] < nums2[j]:
                flag = nums2[j]
                break
            else:
                flag = -1
        a.append(flag)
    return a