# Definition for a binary tree node.
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from copy import copy
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        # prefix_sum 初始化
        # hahsmap backtracking需要
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        res = [0]
        self.dfs(root, 0, targetSum, prefix_sum, res)
        return res[0]
    
    
    def dfs(self, root, pre_sum, targetSum, prefix_sum, res):
        if not root:
            return 
        
        pre_sum += root.val   
        
        if pre_sum - targetSum in prefix_sum:
            res[0] += prefix_sum[pre_sum - targetSum]
            
        
        prefix_sum[pre_sum] += 1
        
        # 把一个变量做全局变量的时候需要backtracking，可以显著的节约时间空间
        # backtracking 回到上一层的hashmap， 用bt的目的就是用一个全局的hashmap然后更新它节约空间和时间 (h*n)
        # 也可以每一层 都用一个hashmap (h)
        
        self.dfs(root.left, pre_sum, targetSum, copy(prefix_sum), res)

        self.dfs(root.right, pre_sum, targetSum, copy(prefix_sum), res)
            