
def mergeTrees(self, t1, t2):
    if t1 is None and t2 is None:
        return None
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    t1.val += t2.val
    t1.right = self.mergeTrees(t1.right, t2.right)
    t1.left = self.mergeTrees(t1.left, t2.left)
    return t1

