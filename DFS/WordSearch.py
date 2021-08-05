'''
a pseudocode template for backtacking
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
'''
def wordSearch(self, matrix, word):
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if self.dfs(matrix, i, j, word, 0):
                return True
    return False

def dfs(self, matrix, i, j, word, index):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    if not (0 <= i < len(matrix) and 0 <= j < len(matrix[0])) or matrix[i][i] != word[index]:
        return False
    if index == len(word) - 1:
        return True
    tmp = matrix[i][j]
    matrix[i][j] = -1
    res = self.dfs(matrix, i + 1, j, word, index + 1) \
    or self.dfs(matrix, i - 1, j, word, index + 1) \
    or self.dfs(matrix, i, j + 1, word, index + 1) \
    or self.dfs(matrix, i, j - 1, word, index + 1)
    matrix[i][j] = tmp
    return res

    
