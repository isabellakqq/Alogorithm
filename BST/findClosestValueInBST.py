def findClosestValueInBst(tree, target):
    return helper(tree,target,tree.value)
def helper(tree,target,closest):
	cur_node=tree
	while cur_node:
		if abs(target-closest)>abs(target-cur_node.value):
			closest=cur_node.value
		if target<cur_node.value:
			cur_node=cur_node.left
		elif target>cur_node.value:
			cur_node=cur_node.right
		else:
			break
	return closest
	

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
