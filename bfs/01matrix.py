from collections import deque
class Solution:
    def updateMatrix(self, mat):
        '''
        clarify: input: 2D array, out put: 2D array, inplace? There is at least one 0 in mat.

        Assumption:if mat[i][j] == 0: distance_to_nearest_zero[i][j] = 0 else bfs d += 1
        Rest: 
            bfs to find nearest 0 and  return distance,
            use deque
            use hashmap to mapping (x, y) to the distance of other point to (x, y) and Prevent repeated visits
           
        Test: time and space: o(m * n)
        
            [0,0,0],
            [0,1,0],
            [1,1,1]
    
        '''
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    mat[i][j] = self.bfs(mat, i, j)
        return mat
    def bfs(self, mat, x, y):
        q = deque([(x, y)])
        distance = {(x, y): 0}
        while q:
            x, y = q.popleft()
            if mat[x][y] == 0:
                return distance[(x, y)]
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nextX, nextY = x + dx, y + dy
                if (nextX, nextY) in distance:
                    continue
                if 0 <= nextX < len(mat) and 0 <= nextY < len(mat[0]):
                    distance[(nextX, nextY)] = distance[(x, y)] + 1
                    q.append((nextX, nextY))
     
            
        
        
        