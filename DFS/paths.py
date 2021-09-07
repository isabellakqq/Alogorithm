def num_of_paths_to_dest(n):
    memo = {}
    return dfs(0, 0, n, memo)

def dfs(i, j, n, memo):
    if (i, j) in memo:
        return memo[(i, j)]
    if i == n - 1 and j == n - 1:
        return 1
    res = 0
    if is_valid(i + 1, j, n):
        res += dfs(i + 1, j, n, memo)
    if is_valid(i, j + 1, n):
        res += dfs(i, j + 1, n, memo)
    memo[(i, j)] = res
    print(memo)
    return res
def is_valid(i, j, n):
    if i < j:
        return False
    if i >= n or j >= n:
        return False
    return True
n = 4
print(num_of_paths_to_dest(1))