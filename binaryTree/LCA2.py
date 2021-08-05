# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        p , q is not same
        all unique
        p, q maynot exist
        
        '''
        solu = self.helper(root, p, q)
        if not solu:
            return None
        else:
            if solu == p:
                if not self.helper(p, q, q):
                    return None
                return p
            if solu == q:
                if not self.helper(q, p, p):
                    return None
                return q
        return solu
            
    def helper(self, root, p, q):
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.helper(root.left, p, q)
        right = self.helper(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        if left and right:
            return root
        
    