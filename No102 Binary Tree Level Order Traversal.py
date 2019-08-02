#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/2 12:17
@File    : No102 Binary Tree Level Order Traversal
@Software: PyCharm
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        stack = [root]
        num = 1
        while stack or num:
            temp = []
            count = 0
            for i in range(num):
                node = stack.pop(0)
                temp.append(node.val)
                if node.left:
                    stack.append(node.left)
                    count += 1
                if node.right:
                    stack.append(node.right)
                    count += 1
            result.append(temp)
            num = count
        return result