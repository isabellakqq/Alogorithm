# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        '''
        从上往下传的值是path * 10 + root.val
        d(4) 
       /   \
      d(9) 4
     /   \
   d(5) 40 + 9  当前层是叶子节点：490 + 5 加入到全局变量self.res里
    /
return 
[(5, 49)] 
        '''
        self.res = 0
        self.dfs(root, 0)
        return self.res
    def dfs(self, root, path):
        if not root:
            return
        if not root.left and not root.right:
            path = path * 10 + root.val
            self.res += path
        self.dfs(root.left, path * 10 + root.val )
        self.dfs(root.right, path * 10 + root.val)
    
class solution2:
    def sumToroot(self, root):
        if not root:
            return 0
        res = 0
        stack = [(root, 0)]
        while stack:
            node, cur_number = stack.pop()
            if node:
                cur_number = cur_number * 10 + node.val
                #if it's a leaf node, sum up res
                if not node.left and not node.right:
                    res += cur_number
                else:
                    stack.append((root.right, cur_number))
                    stack.append((root.left, cur_number))