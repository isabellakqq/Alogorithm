import collections
from typing import List
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        # {0 : [1], 1 : [0, 2, 4], 2 : [3, 1], 3 : [2], 4 : [1, 5]}
        #无向无环连通图找最长路径用pre去重
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        self.diameter = 0
        self.dfs(graph, 0, None)
        return self.diameter
    
    def dfs(self, graph, node, pre):
        d1 = d2 = 0
        for nex in graph[node]:
            if nex != pre:
                d = self.dfs(graph, nex, node)
                if d > d1:
                    d1, d2 = d, d1
                elif d > d2:
                    d2 = d
        self.diameter = max(self.diameter, d1 + d2)
        return d1 + 1
