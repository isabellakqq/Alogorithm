import collections
def hasPath(self, maze, start, destination):
        #corner case and sanity check
        if not maze or not start or not destination:
            return False
        if start == destination:
            return True
        m, n = len(maze), len(maze[0])
        q = collections.deque([start])
        visited = set()
        while q:
            cur = q.popleft()
            if cur[0] == destination[0] and cur[1] == destination[1]:
                return True
            for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x = cur[0] + d[0]
                y = cur[1] + d[1]
                while 0 <= x < m and 0 <= y < n and maze[x][y] == 0:
                    x += d[0]
                    y += d[1]
                x -= d[0]
                y -= d[1]
                if (x, y) not in visited:
                    visited.add((x, y))
                    q.append((x, y))
        return False