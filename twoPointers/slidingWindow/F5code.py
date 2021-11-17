'''
input: string
output: ch
example:example:aabcccdee
max_cnt = 
            start
                  i == i + 1
            cur_cnt = i - start + 1
if cur_cnt > max_cnt 
    res = s[start]
    max_cnt = cur_cnt
aabcccdee
   i
s
start
i
time: O(N)
space: O(1)
'''
def get_maxchar(s):
    if not s:
        return ''

    n = len(s)
    res = ''
    start = 0
    max_cnt = 0
    i = 0
    while i < n:
        while i < n - 1 and s[i] == s[i + 1]:
            i += 1
        cur_cnt = i - start + 1
        if cur_cnt > max_cnt:
            res = s[start]
            max_cnt = cur_cnt
        i += 1
        start = i 
    return res
s = 'b'
print(get_maxchar(s))
