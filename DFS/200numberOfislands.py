'''
[[6, 0, 3]
 [2, 0, 0]
 [0, 8, 1]]
'''
def get_max(matrix):
    m, n = len(matrix), len(matrix[0])
    visited = set()
    max_value = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] and (i, j) not in visited:
                sums = [0]
                dfs(matrix, i, j, visited, sums)
                max_value = max(max_value, sums[0])
    return max_value

def dfs(matrix, i, j, visited, sums):
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] == 0 or (i, j) in visited:
        return 
    sums[0] += matrix[i][j]
    visited.add((i, j))
    dfs(matrix, i + 1, j, visited, sums)
    dfs(matrix, i - 1, j, visited, sums)
    dfs(matrix, i, j + 1, visited, sums)
    dfs(matrix, i, j - 1, visited, sums)

a = [[6, 0, 3], [2, 0, 0], [0, 8, 1]]
print(get_max(a))