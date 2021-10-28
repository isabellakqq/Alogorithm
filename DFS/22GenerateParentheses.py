def generate_parenthess(n):
    if n == 1:
        return ['()']

    res = []
    dfs(n, n, [], res)
    return res

def dfs(left, right, path, res):
    if right == 0 and left == 0:
        res.append(''.join(path))
        return 

    if left > 0:
        path.append('(')
        dfs(left - 1, right, path, res)
        path.pop()
    if right > left:
        path.append(')')
        dfs(left, right - 1, path, res)
        path.pop()

print(generate_parenthess(3))