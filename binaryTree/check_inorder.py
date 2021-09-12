class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

t1 = TreeNode(5)
t1.left = TreeNode(3)
t1.left.left = TreeNode(1)
t1.right = TreeNode(7)
t1.right.left = TreeNode(6)

t2 = TreeNode(3)
t2.left = TreeNode(1)
t2.right = TreeNode(6)
t2.right.left = TreeNode(5)
t2.right.right = TreeNode(7)

# def check_same(t1, t2):
#     if not t1 or not t2:
#         return False

#     stack1 = []
#     stack2 = []
#     push_left(t1, stack1)
#     push_left(t1, stack2)
#     while stack1 and stack2:
#         node1 = stack1.pop()
#         node2 = stack2.pop()
#         if node1.val != node2.val:
#             return False
#         if node1.right:
#             push_left(node1.right, stack1)
#         if node2.right:
#             push_left(node2.right, stack2)
#     return True
                
# def push_left(node, stack):
#     while node:
#         stack.append(node)
#         node = node.left

class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
t1 = TreeNode(5)
t1.left = TreeNode(3)
t1.left.left = TreeNode(1)
t1.right = TreeNode(7)
t1.right.left = TreeNode(6)

t2 = TreeNode(3)
t2.left = TreeNode(1)
t2.right = TreeNode(6)
t2.right.left = TreeNode(5)
t2.right.right = TreeNode(7)

def check_same(t1, t2):
    if not t1 or not t2:
        return False
    l1 = []
    inorder(t1, l1)
    return check_t2(t2, l1)
    
def inorder(root, res):
    if not root:
        return
    inorder(root.left, res)
    res.append(root.val)
    inorder(root.right, res)

def check_t2(t2, l1):
    if not t2:
        return True
    if not check_t2(t2.left, l1):
        return False
    if not l1 or l1.pop(0) != t2.val:
        return False
    return check_t2(t2.right, l1)
print(check_same(t1, t2))
   
