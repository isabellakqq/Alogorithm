'''
pass by index
Integer[] = [1, 2, 3, 4, 5, null, 7]
int[] 

       1
    /     \ 
  2     3
 / \      / \
4 5   null  7 
			  0

	    x
2*x + 1     2*x + 2	


'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(arr):
    return dfs(arr, 0)

def dfs(arr, index):  
    if not arr:
        return None
    if index >= len(arr):
        return None
    root = TreeNode(arr[index])
    root.left = dfs(arr, 2 * index + 1)
    root.right = dfs(arr, 2 * index + 2)

