class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, u):
        if self.parent[u] != u:
            # path compression
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    # 1: 判断之前知否相连如果不是就连在一起   
    def union(self, u, v):
        parent_of_u = self.find(u)
        parent_of_v = self.find(v)
        # 在这之前就是connected的
        if  parent_of_u ==  parent_of_v:
            return True
        else:
            self.parent[parent_of_u] =  parent_of_v
            return False
            
            
    

def findRedundantConnection(edges):
    uf = UnionFind(len(edges))
    for i, j in edges:
        if uf.union(i - 1, j - 1):
            return [i, j]
    
print(findRedundantConnection(edges=[[1,2],[1,3],[2,3]]))