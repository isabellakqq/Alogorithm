from collections import deque
def rottingOranges(self, grid):
    '''
    多源点bfs把所有烂橘子都放到队列里作为源点进行bfs
    
    '''
    if not grid or not grid[0]:
        return 0
    res, cnt_fresh = 0, 0
    m, n = len(grid), len(grid[0])
    q = deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                q.append((i, j, 0))
            if grid[i][j] == 1:
                cnt_fresh += 1
    if not cnt_fresh:
        return 0
    while q:
        r, c, times = q.popleft()
        res = times
        for d in [(0, 1), (0, -1), (1, 0), (1, -1)]:
            x, y = r + d[0], c + d[1]
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                grid[x][y] = 2
                q.append((x, y, times + 1))
                cnt_fresh -= 1
    return res if not cnt_fresh else -1
