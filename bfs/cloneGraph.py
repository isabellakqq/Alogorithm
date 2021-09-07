import collections
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    '''
    clarify：not node:return None
    易错点1:揉在一起写
    2: q.append(neighbor)
    '''
    def cloneGraph(self, node: 'Node') -> 'Node': 
        if not node:
            return None
        # step1: find nodes
        nodes = self.find_nodes_by_bfs(node)
        # step2: copy nodes
        old2new = self.copy_nodes(nodes)
        # step3: copy edges
        self.copy_edges(nodes, old2new)
        
        return old2new[node]
        
    def find_nodes_by_bfs(self, node):
        visited = set([node])
        q = collections.deque([node])
        while q:
            cur_node = q.popleft()
            for neighbor in cur_node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        return list(visited)
    
    def copy_nodes(self, nodes):
        mapping = {}
        for node in nodes:
            mapping[node] = Node(node.val)
        return mapping
    
    def copy_edges(self, nodes,old2new):
        for node in nodes:
            new_node = old2new[node]
            for neighbor in node.neighbors:
                new_neighbor = old2new[neighbor]
                new_node.neighbors.append(new_neighbor)
    