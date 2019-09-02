#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/2 13:53
@File    : No513 Find Bottom Left Tree Value
@Software: PyCharm
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        stack = [root]
        count, num = 1, 0
        result = ()
        temp = []
        while stack:
            while count > 0:
                count -= 1
                node = stack.pop(0)
                temp.append(node.val)
                if node.left:
                    stack.append(node.left)
                    num += 1
                if node.right:
                    stack.append(node.right)
                    num += 1
            result = temp[0]
            count = num
            num = 0
            temp = []
        return result