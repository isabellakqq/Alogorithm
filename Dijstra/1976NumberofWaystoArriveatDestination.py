from collections import defaultdict
from typing import List
import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for i, j, time in roads:
            graph[i][j] = time
            graph[j][i] = time
        print(graph)
        min_heap = [(0, 0)] # total time, node
        ways = [0] * n
        ways[0] = 1
        costs = [float('inf')] * n
        costs[0] = 0
        while min_heap:
            node_time, node = heapq.heappop(min_heap)
            if node_time > costs[node]:
                continue
            for next_node, next_time in graph[node].items():
                new_time = node_time + next_time
                if new_time > costs[next_node]:
                    continue
                elif new_time == costs[next_node]:
                    ways[next_node] += ways[node]
                else:
                    costs[next_node] = new_time
                    ways[next_node] = ways[node]
                    heapq.heappush(min_heap, (new_time, next_node))
        return ways[-1] % (10**9 + 7)

s = Solution()
test = s.countPaths(7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1]])
print(test)

        