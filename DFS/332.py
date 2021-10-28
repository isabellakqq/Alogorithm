from collections import defaultdict
from heapq import heappop, heappush
import heapq
from typing import List
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        '''
        post_order traversal each Edges
        遍历每条边用过的就扔掉
        区别：
        pre_order do sth -> dfs
        post_order dfs -> do sth
        先考虑后面所有的可能性再考虑当前答案
        '''
        graph = defaultdict(list)
        #build graph
        for i, j in tickets:
            heapq.heappush(graph[i], j)
        
        # do dfs
        res = []
        self.dfs('JFK', graph, res)
        return res[::-1]
    
    def dfs(self, node, graph, res):
        
        # post-order 
        while graph[node]:
            # next_node pop from heap
            next_node = heapq.heappop(graph[node])
            # dfs
            self.dfs(next_node, graph, res)
        res.append(node)
        
        