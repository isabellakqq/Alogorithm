from typing import _Collection, List


import collections
class Solution:
    DIRECTION = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m, n = len(matrix), len(matrix[0])
        outdegree = [[0] * n for _ in range(m)]

        queue = collections.deque()

        for r in range(m):
            for c in range(n):
                for dir in self.DIRECTION:
                    x, y = r + dir[0], c + dir[1]
                    if x < 0 or x >= m or y < 0 or y >= n:
                        continue
                    
                    if matrix[x][y] > matrix[r][c]:
                        outdegree[r][c] += 1
                
                if outdegree[r][c] == 0:
                    queue.append((r, c))
        
        result = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                cur_row, cur_col = queue.popleft()

                for dir in self.DIRECTION:
                    x, y = cur_row + dir[0], cur_col + dir[1]
                    if x < 0 or x >= m or y < 0 or y >= n:
                        continue
                    
                    if matrix[x][y] < matrix[cur_row][cur_col]:
                        outdegree[x][y] -= 1
                        if outdegree[x][y] == 0:
                            queue.append((x, y))
            result += 1
            
        return result