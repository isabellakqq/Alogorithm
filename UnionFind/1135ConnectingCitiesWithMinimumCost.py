from typing import List


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
    
    def find(self, u):
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])
            
        return self.parents[u]
    
    def union(self, u, v):
        parent_of_u = self.find(u)
        parent_of_v = self.find(v)
        if parent_of_u == parent_of_v:
            return True
        else:
            self.parents[parent_of_u] = parent_of_v
            return False

def minimumCost(n: int, connections: List[List[int]]) -> int:
    uf = UnionFind(n)
    connections.sort(key = lambda x : x[2], reverse = True)
    print(connections)
    cnt = 1
    res = 0
    while connections:
        i, j, cost = connections.pop()
        if not uf.union(i - 1, j - 1):
            cnt += 1
            res += cost
    return res if cnt == n else -1
            
            
connections = [[1,2,5],[1,3,6],[2,3,1]]
print(minimumCost(3, connections))