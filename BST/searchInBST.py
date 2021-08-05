from class import TreeNode
def searchInBST(self, root, val):
    if root.val == val:
        return root
    elif root.val > val:
        return self.searchInBST(root.left)
    else:
        return self.searchInBST(root.right)
    # while root:
    #     if root.val == val:
    #         return root
    #     elif root.val > val:
    #         root = root.left
    #     else:
    #         root = root.right
    # return -1