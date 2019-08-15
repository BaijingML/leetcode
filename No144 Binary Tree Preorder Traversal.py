#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/15 9:13
@File    : No144 Binary Tree Preorder Traversal
@Software: PyCharm
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.result = []
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            self.result.append(root.val)
            self.helper(root.left)
            self.helper(root.right)
        return self.result
    def helper(self, node):
        if node:
            self.result.append(node.val)
            self.helper(node.left)
            self.helper(node.right)

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        result = []
        if root:
            while stack or root:
                while root:
                    result.append(root.val)
                    stack.append(root)
                    root = root.left
                if stack:
                    node = stack.pop(-1)
                    root = node.right
        return result
