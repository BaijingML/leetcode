# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        result = 0

        def helper(node, temp):
            if not node:
                return 0
            temp = temp * 2 + int(node.val)
            if not node.left and not node.right:
                return temp
            return helper(node.left, temp) + helper(node.right, temp)

        return helper(root, result)
