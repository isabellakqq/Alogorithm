import collections
'''
DAG directed acylic graph 有向无环图用拓扑排序
method1: indegree expand from indegree = 0
approach2: dfs outdgree visited and onStack if node.nb onStack 有环return False
'''

class Solution:
    def findOrder(self, numCourses, prerequisites):
        indegree = collections.defaultdict(int)
        graph = collections.defaultdict(list)
        for i, j in prerequisites:
            indegree[i] += 1
            graph[j].append(i)
        start_nodes = [n for n in range(numCourses) if indegree[n] == 0]
        q = collections.deque(start_nodes)
        ordering = []
        while q:
            node = q.popleft()
            ordering.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return ordering if len(ordering) == numCourses else []
s = Solution()
print(s.findOrder(4,[[1,0],[1,2],[0,1]]))
# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         '''
#         node 2  indegree 
#         put indgree[node] == 0 into q
#         for node in node.neighbour
#         time: O(V + E)
#         space:O(V + E)
#         '''
#         node_to_indgree = collections.defaultdict(int)
#         graph = collections.defaultdict(list)
        
#         # build graph and mapping
#         for i, j in prerequisites:
#             node_to_indgree[i] += 1
#             graph[j].append(i)
            
#         # put start node into q 
#         start_node = [n for n in range(numCourses) if node_to_indgree[n] == 0]
#         q = collections.deque(start_node)
        
#         # bfs
#         ordering = []
#         while q:
#             node = q.popleft()
#             ordering.append(node)
#             for neighbor in graph[node]:
#                 node_to_indgree[neighbor] -= 1
#                 if node_to_indgree[neighbor] == 0:
#                     q.append(neighbor)
#         return ordering if len(ordering) == numCourses else []
        
        