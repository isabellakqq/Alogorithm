class BT:
    def isBalancedBianryTree(self, root):
        if not root:
            return True
        is_balanced, height = self.dfs(root)
        return is_balanced
    def dfs(self, root):
        if not root:
            return True, 0
        left_isBalanced, left_height = self.dfs(root.left)
        right_isBanlanced, right_height = self.dfs(root.right)
        root_height = max(left_height, right_height) + 1
        if not left_isBalanced or not left_isBalanced:
            return False, root_height
        if abs(left_height - right_height) > 1:
            return False, root_height
        return True, root_height


