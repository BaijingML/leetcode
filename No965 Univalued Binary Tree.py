# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        if root.right:
            if root.val != root.right.val:  # Equavalent
                return False

        if root.left:
            if root.val != root.left.val:  # Equavalent
                return False

        return self.isUnivalTree(root.right) and self.isUnivalTree(root.left)