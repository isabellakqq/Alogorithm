# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections
from typing import List
class Solution:
    '''
    level order by dfs use list[deque]
    '''
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.dfs(root, 0, res)
        return res
    
    def dfs(self, root, level, res):
        if not root:
            return 
        if len(res) == level:
            res.append(collections.deque())
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].appendleft(root.val)
            self.dfs(root.left, level + 1, res)
            self.dfs(root.right, level + 1, res)
        # if not root:
        #     return res
        # q = collections.deque()
        # flag = True
        # q.append(root)
        
        # while q:
        #     size = len(q)
        #     tmp = []
        #     for i in range(size):
        #         node = q.popleft()
        #         tmp.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     if not flag:
        #         tmp.reverse()
        #     res.append(tmp)
            
        #     flag = not flag
        # return res