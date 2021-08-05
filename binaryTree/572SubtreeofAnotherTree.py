from class import TreeNode
def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
    if not s: 
        return not t
    if self.isSameTree(s, t): 
        return True
    return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p and q:
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)