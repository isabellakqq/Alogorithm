class TreeNode:
    def __init__(self, val = None, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right
class Soution:
    def deletNode(self, root:TreeNode, key:int) -> TreeNode:
        if not root:
            return root
        #case1 key in left delete in left
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        #case2 key in right delete in right
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        #find the key
        else:
            #case1 only have left 
            if not root.right:
                return root.left
            #case1 only have right
            elif not root.left:
                return root.right
            #both left and right
            else:
                minNode = self.findMin(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
        return root
    def findMin(self, root):
        while root.left:
            root = root.left
        return root

                
                
                

