from collections import deque
def isBipartite(self, graph):

    """
    node from 0-n-1,and edges in garph
    bfs1
    Data structure:maintain a FIFO queue, put all generated neighbor nodes in the queue
    process:set(A) color to 1 and Set(B) color to 0 in hashmap to distinguish
    Terminate condition: if the any of one neighbor node'color equal to the second then return False, do a loop until the queue is empty return True
    Test: color :{0 : 1, 1: 0, 3:0, 2:1} q[1,3]
    
    """
    
    n = len(graph)
    color = {}
    for i in range(n):
        if i not in color:
            q = deque([i])
            color[i] = 1
            while q:
                node = q.popleft()
                for nb in graph[node]:
                    if nb not in color:
                        color[nb] = 1 - color[node]
                        q.append(nb)
                    elif color[nb] == color[node]:
                        return False
    return True
    #dfs use stack
#         colors = {}
        
#         for node in range(len(graph)):
#             if node in colors:
#                 continue
#             stack = [node]
#             colors[node] = 0
#             while stack:
#                 node = stack.pop()
#                 for nei in graph[node]:
#                     if nei not in colors:
#                         colors[nei] = 1 - colors[node]
#                         stack.append(nei)
#                     elif colors[nei] == colors[node]:
#                         return False
#         return True