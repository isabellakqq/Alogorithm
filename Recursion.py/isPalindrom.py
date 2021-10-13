def isPalindrom(s, i, j):
    if i == j:
        return True
    if i + 1 == j:
        return s[i] == s[j]
    if s[i] != s[j]:
        return False
    return isPalindrom(s, i + 1, j - 1)
print(isPalindrom('baa', 0, 2))
    