class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s: return False
        if not t: return True
        if self.hasTree(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def hasTree(self, s, t):
        if (not s and t) or (s and not t):
            return False
        elif not s and not t:
            return True
        else:
            if s.val == t.val:
                return self.hasTree(s.left, t.left) and self.hasTree(s.right, t.right)
            else:
                return False