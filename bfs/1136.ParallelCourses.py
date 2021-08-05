from typing import List
import collections
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        '''
        Step 1: Build a directed graph from relations.
        Step 2: Record the in-degree of each node. (i.e., the number of edges towards the node)
        Step 3: Initialize a queue, queue. Put nodes with an in-degree of 0 into queue. Initialize step = 0, visited_count = 0.
        Step 4: Start BFS: Loop until queue is empty
        Step 5: If visited_count == N, return step. Otherwise, return -1.
        '''
        indegree = collections.defaultdict(int)
        graph = collections.defaultdict(list)
        for n1, n2 in relations:
            graph[n1].append(n2)
            indegree[n2] += 1
        
        q = collections.deque()
        for node in range(1, n + 1):
            if indegree[node] == 0:
                q.append(node)
        if len(q) == 0:
            return -1
        cnt_semesters = 0
        cnt_studied = 0
        while q:
            cnt_semesters += 1
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                cnt_studied += 1
                for nb in graph[node]:
                    indegree[nb] -= 1
                    if indegree[nb] == 0:
                        q.append(nb)
        return cnt_semesters if cnt_studied == n else -1
        