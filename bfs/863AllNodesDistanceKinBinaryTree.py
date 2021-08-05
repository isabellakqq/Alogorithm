from class import TreeNode
import collections
from typing import List
def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        '''
        step1 buid non-directed graph set_parents
        step2 bfs level order tarvasal 
        '''
        self.set_parents(root, None)
        q = collections.deque([target])
        seen = set([target])
        level = 0
        while q:
            if level == k:
                break
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                for nb in [node.left, node.right, node.parent]:
                    if nb and nb not in seen:
                        q.append(nb)
                        seen.add(nb)
            level += 1
        return [node.val for node in q]
    
def set_parents(self, root, parent):
    if not root:
        return 
    root.parent = parent
    self.set_parents(root.left, root)
    self.set_parents(root.right, root)
    