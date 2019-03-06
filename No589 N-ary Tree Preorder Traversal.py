class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        else:
            result = [root.val]
            for i in root.children:
                result.extend(self.preorder(i))
            return result