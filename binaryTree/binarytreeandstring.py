'''
               root(20): 
left 5(abcde)              right(15):            
             left(10) (fghijklmno)       right(pqrst)
                            5 - 
                            8 - （10 - 5）
inorder root left - right
'''
import collections
class TreeNode:
    def __init__(self, word, lens) -> None:
        self.word = word
        self.lens = lens
        self.left = None
        self.right = None
class Amazon:
    def find_nth(self,root, n):
        # corner case 要和面试官交流加分项
        if not root:
            return ''
        if root.lens < n:
            return ''
        # leaf node
        if not root.left and not root.right:
            return root.word[n-1] 
        #  left root.left.lens >= n 
        if root.left and root.left.lens >= n:
            return self.find_nth(root.left, n)
        # left root.left.lens >= n 
        elif root.left: 
            return self.find_nth(root.right, n - root.left.lens)
        # no left 
        else:
            return self.find_nth(root.right, n)
    def find_word(self, root, n, k):
        # base case
        if not root:
            return ''
        if root.lens < n:
            return ''
        if k <= 0:
            return ''
        # 
        if not root.left and not root.right:
            # 不够长
            if root.lens - n < k:
                return root.word[n:]
            # 够长
            else:
                return root.word[n : n + k]
        res = ''
        if root.left:
            res =  self.find_word(root.left, n, k)
            res += self.find_word(root.right, max(0, n - root.left.lens), k - len(res))
        # 没有left
        else:
            res += self.find_word(root.right, n, k)
        return res 

tree = TreeNode(None, 20)    
t1 = TreeNode('ABCDE', 5) 
t2 = TreeNode(None, 15)
t3 = TreeNode('FGHIJKLMNO', 10)
t4 = TreeNode('PQRST', 5)
tree.left = t1
tree.right = t2
t2.left = t3
t2.right = t4
test = Amazon()
print(test.find_nth(tree, 10))
print(test.find_word(tree, 10, 8))

