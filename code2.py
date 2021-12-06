'''
input: Linkedlist unknow size
ouput: Node 3
eg: 1->2-> 3->4->5       kth from last 3
        slow   fast
step1:
while k > 0:    
step2: 



2: coordinate of matrix (left right) and (right left):
total area combinde 
rebase to version


sd 

'''
# from datetime import datetime
# s2 = '01:09'
# s1 = '00:10'
# format = '%M:%S'
# print(datetime.strptime(s1, format))
# time = datetime.strptime(s2, format) - datetime.strptime(s1, format)
# print(str(time).split(':')[-1])
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
root = TreeNode(10)
node1 = TreeNode(2)
node2 = TreeNode(8)
root.left = node1
root.right = node2
import collections
def collect(root):
    q = collections.deque(((root, 0),))
    while q:
        node, h = q.popleft()
        if node.left:
            q.append((node.left, h + 1))
        if node.right:
            q.append((node.right, h + 1))
    return h

print(collect(root))
