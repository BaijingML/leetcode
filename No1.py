# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 14:07:46 2017

@author: ZFS
"""

nums = [2,5,5,11]
target = 10
#for i in range(len(nums)):
#    for j in range(i+1,len(nums)):
#        if nums[j] == target-nums[i]:
#            a = nums.index(nums[i])
#            b = nums.index(nums[j],-1)
#        if nums[j] == target-nums[i]:
#            if nums[i] == nums[j]:
#                a = nums.index(nums[i])
#                del nums[a]
#                b = nums.index(nums[j-1])+1
#                nums.insert(a,nums[i])
#            else:
#                a = nums.index(nums[i])
#                b = nums.index(nums[j])
#            print([a,b])
#        else:
#            pass
for index,item in enumerate(nums):
    print(index,item)
    if target-item in nums:
        
        a = index
        b = nums.index(sub)
    