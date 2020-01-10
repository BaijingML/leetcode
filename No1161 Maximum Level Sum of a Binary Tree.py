#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/10/11 16:07
@File    : No1161 Maximum Level Sum of a Binary Tree
@Software: PyCharm
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxLevelSum(self, root):
        if not root:
            return 0
        max_level = 0
        max_sum = root.val
        level_index = 0
        num = 1
        count = 0
        stack = [root]
        while stack:
            temp = 0
            level_index += 1
            while num > 0:
                num -= 1
                node = stack.pop(0)
                if node.left:
                    stack.append(node.left)
                    count += 1
                if node.right:
                    stack.append(node.right)
                    count += 1
                temp += node.val
            if temp > max_sum:
                max_level = level_index
                max_sum = temp
            num = count
            count = 0
        return max_level
