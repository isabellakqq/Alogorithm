"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        hp = self.get_height(p)
        hq = self.get_height(q)
        #2 
        while hq > hp:
            q = q.parent
            hq -= 1
        while hp > hq:
            p = p.parent
            hp -= 1
        while p != q:
            p = p.parent
            q = q.parent
        return p
    def get_height(self, node):
        h = 0
        cur = node
        while cur.parent:
            cur = cur.parent
            h += 1
        return h
            
       
        