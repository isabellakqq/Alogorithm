from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        '''
        最坏情况每个点都有边2^(n-2)*n
        Input: graph = [[1,2],[3],[3],[]]
        Output: [[0,1,3],[0,2,3]]
        Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
        clarify: is there a circle/ring in the graph ?
                 Is it a directed graph?
                 connected?
                how many nodes in the graph
    
        '''
        visited = set()
        res = []
        self.dfs(graph, 0,  [],  res, visited)
        return res
        
    def dfs(self, graph, node,  path, res, visited):
        visited.add(node)
        path.append(node)
        if node == len(graph) - 1:
            res.append(path[:])
            return 
        for next_node in graph[node]:
            if next_node not in visited:
                visited.add(next_node)
                self.dfs(graph, next_node,  path, res, visited)
                visited.remove(next_node)
                path.pop()
        