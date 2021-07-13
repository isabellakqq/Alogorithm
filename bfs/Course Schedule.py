from collections import defaultdict, deque
def canFinish(self, numCourses, prerequisites):
        indegree = defaultdict(int)
        edges = defaultdict(list)
        n = 0
        for i, j in prerequisites:
            indegree[i] += 1
            edges[j].append(i)
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        while q:
            course = q.popleft()
            n += 1
            for next_c in edges[course]:
                indegree[next_c] -= 1
                if indegree[next_c] == 0:
                    q.append(next_c)
        return n == numCourses
                