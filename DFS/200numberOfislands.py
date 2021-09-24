'''
[[6, 0, 3]
 [2, 0, 0]
 [0, 8, 1]]
 hashset时间空间比较浪费，resize重新赋值一遍, hashclision 75% capacity
 用arr比较好
'''
def get_max(matrix):
    m, n = len(matrix), len(matrix[0])
    visited = [[False]*n for _ in range(m)]
    max_value = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] and not visited[i][j]:
                sums = [0]
                dfs(matrix, i, j, visited, sums)
                max_value = max(max_value, sums[0])
    return max_value

def dfs(matrix, i, j, visited, sums):
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] == 0 or visited[i][j]:
        return 
    sums[0] += matrix[i][j]
    visited[i][j] = True
    dfs(matrix, i + 1, j, visited, sums)
    dfs(matrix, i - 1, j, visited, sums)
    dfs(matrix, i, j + 1, visited, sums)
    dfs(matrix, i, j - 1, visited, sums)

a = [[6, 0, 3], [2, 0, 0], [0, 8, 1]]
print(get_max(a))