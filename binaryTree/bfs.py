class Solution(object):
  def isBST(self, root):
    """
    input: TreeNode root
    return: boolean
    """
    # write your solution here
    if not root:
      return True
    return self.helper(root, float("-inf"), float("inf"))
  def helper(self, root, Min, Max):
    if not root:
      return True
    #remeber to include '=' bst can't == left.val or right.val clarify with interviwer what is a bst can be equal or not
    if root.val >= Max or root.val <= Min:
      return False

    return self.helper(root.right, root.val, Max) and self.helper(root.left, Min, root.val)