
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        return的top2 max1, max2, 每一层都和最大值打个擂台
        tree有向无环图
        """
        self.res = 0
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        if not root:
            return 0
        max1, max2 = 0, 0
        for child in root.children:
            depth = self.dfs(child)
            if depth > max1:
                max2 = max1
                max1 = depth
                
            elif depth > max2:
                max2 = depth
        self.res = max(self.res, max1 + max2)
        return max1 + 1