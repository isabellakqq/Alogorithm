def countUnivalSubtrees(self, root) -> int:
    if not root:
        return 0
    cnt = [0]
    self.helper(root, cnt)
    return cnt[0]
    
def helper(self, root, cnt):
    if not root:
        return 
    
    left = self.helper(root.left, cnt)
    right = self.helper(root.right, cnt)
    if (not left or left == root.val) and (not right or right == root.val):
        cnt[0] += 1
        return root.val
    return '#'
    