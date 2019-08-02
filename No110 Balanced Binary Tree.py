# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        def height(node):
            if node.left and node.right:
                return max(height(node.left), height(node.right)) + 1
            elif node.left:
                return height(node.left) + 1
            elif node.right:
                return height(node.right) + 1
            else:
                return 0
        left = 0
        right = 0
        if root.left:
            left = height(root.left) + 1
        if root.right:
            right = height(root.right) + 1
        return -1 <= right - left <= 1