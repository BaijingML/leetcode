# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.Leaf(root1) == self.Leaf(root2)
    def Leaf(self, root):
        node_list = [root]
        leaf = []
        while node_list:
            node = node_list.pop(0)
            if node.right:
                node_list.insert(0, node.right)
            if node.left:
                node_list.insert(0, node.left)
            if (not node.left) and (not node.right):
                leaf.append(node.val)
        return leaf
