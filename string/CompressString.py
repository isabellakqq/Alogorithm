def compress(s):
    if not s:
        return s
    slow = 0
    fast = 0
    res = ''
    n = len(s)
    while slow < n:
        while fast < n and s[slow] == s[fast]:
            fast += 1
        res += s[slow]
        repeated_occur = fast - slow
        if repeated_occur > 1:
            res += str(repeated_occur)
        slow = fast
    return res
string = 'aaabbbcdde'
print(compress(string))