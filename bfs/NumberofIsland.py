from collections import deque
def numIslands(self, grid):
    m = len(grid)
    n = len(grid[0])
    islands = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":  
                grid[i][j] = "#"
                self.bfs(grid, i, j)
                islands += 1 
    return islands 
def bfs(self, grid, i, j):
    m = len(grid)
    n = len(grid[0])
    q = deque([(i, j)])
    while q:
        r, c = q.popleft()
        for d in [(0,1), (0,-1), (-1,0), (1, 0)]:
            new_r, new_c = r + d[0], c + d[1]
            if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c] == "1":
                q.append((new_r, new_c))
                grid[new_r][new_c] = '#'
