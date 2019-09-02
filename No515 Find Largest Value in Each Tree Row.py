#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/2 13:46
@File    : No515 Find Largest Value in Each Tree Row
@Software: PyCharm
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        stack = [root]
        count = 1
        if not root:
            return []
        result = []
        num = 0
        temp = []
        while stack and root:
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
            result.append(max(temp))
            temp = []
            count = num
            num = 0
        return result
