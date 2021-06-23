class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetricTree(self, root):
        if not root:
            return True
        
        return self.helper(root.left, root.right)
       

    def isIdentical(self, node1, node2):
        if not node1 and node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        return self.isIdentical(node1.left, node2.right) and self.isIdentical(node1.right, node2.left)
    
    def test(self):
         print(self.isSymmetricTree([1,2,2,3,4,4,3]))