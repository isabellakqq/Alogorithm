# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
clarify:
result:
        my dfs func return the height of cur node
return 
dfs left subtree maxlength to root node


'''
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = [0]
        self.dfs(root, res)
        return res[0]
    def dfs(self, root, res):
        if not root:
            return 0
        left = self.dfs(root.left, res)#return left_height
        right = self.dfs(root.right, res)#return right_height
        res[0] = max(res[0], left + right)
        return max(left, right) + 1
        