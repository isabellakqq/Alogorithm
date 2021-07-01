from collections import deque
class Solution:
    def updateMatrix(self, mat):
        '''
        clarify: input: 2D array, out put: 2D array, inplace? There is at least one 0 in mat.

        Assumption: 
        Rest: 
            use queue bfs and update every point value to distace to 0 point
            Treat all 0s as starting points
        Test: 
        
            [0,0,0],
            [0,1,0],
            [1,1,1]
    
        '''
        q = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = float('inf')
        while q:
            r, c = q.popleft()
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x = dx + r
                y = dy + c
                if 0 <= x < len(mat) and 0 <= y < len(mat[0]):
                    if mat[x][y] > mat[r][c]:
                        mat[x][y] = mat[r][c] + 1
                        q.append((x, y))
        return mat
    
            
        
        
        