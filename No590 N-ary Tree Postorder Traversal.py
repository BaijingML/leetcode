"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        else:
            result = []
            res = []
            for i in root.children:
                res.extend(self.postorder(i))
            result.extend(res)
            result.append(root.val)
        return result