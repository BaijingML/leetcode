class Solution:
    x_p = None
    x_l = 0
    y_p = None
    y_l = 0

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        self.dfs(root, x, y, 0, None)
        return self.x_p != self.y_p and self.x_l == self.y_l

    def dfs(self, root, x, y, l, node):
        if root.val == x:
            self.x_p = node
            self.x_l = l
        if root.val == y:
            self.y_p = node
            self.y_l = l
        if root.left:
            self.dfs(root.left, x, y, l + 1, root)
        if root.right:
            self.dfs(root.right, x, y, l + 1, root)