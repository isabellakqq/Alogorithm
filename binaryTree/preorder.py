# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        '''
        at most 2 child
        iterator 不是典型的线性数据结构
        base case: root == None: return 
       
        recursive rule: expect return value from left and right inorderTraverse(leftsubtree), inorderTraverse(rightsubtree)
        time :O(N) touch each node once
        space: O(h) height of the tree
        '''
        
        res = []
        if not root:
            return res
        self.dfs(root, res)
        return res
    
    def dfs(self, root, res):
        if not root:
            return 
        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)
