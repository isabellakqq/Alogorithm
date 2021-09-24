from collections import deque
class Solution:
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    self.dfs(grid, i, j)
        return islands

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
            return 
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
        
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
s = Solution()
test = s.numIslands(grid)
print(test)
    
