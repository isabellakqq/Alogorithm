# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        '''
        clarify: input a refrence root of a tree; 
                 output length of univalue path 
                 用的时候可以用left and right ,返回的时候只能返回单边，所以要更新res[0]
        Assumption: if not root  return 0
        res:dfs to traversal tree and return UP pass through the root.left and root.right.
            recursion way: dfs(left) dfs(right)
                            current level:
                                          if left.val == root.val : 1 +left_path
                                          if right == root.val: 1+right_path
                                          update result 
                                          return: max(left_path, right_path)
                                
        Recursive Tree
                            dfs(1)  (2, 1)
                     /                     \
        res[0] = 2 dfs(4)(1,4)                 dfs(5)(1, 5)
         (0) /           \(0)          /       \(0, 5)
          dfs(4)        dfs(4)      return 0 None   dfs(5)
          / \                                          / \
return 0                                       ...
        
        '''
        res = [0]
        self.dfs(root, res)
        return res[0]
    
    def dfs(self, root, res):
        if not root:
            return 0
        l = self.dfs(root.left, res)
        r = self.dfs(root.right, res)
        pl, pr = 0, 0
        if root.left and root.val == root.left.val:
            pl = l + 1
        if root.right and root.val == root.right.val:
            pr = r + 1
        res[0] = max(res[0], pl + pr)
        return max(pl, pr)
        
        
            
            
       