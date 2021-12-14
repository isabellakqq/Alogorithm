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
# def get_maxchar(s):
#     if not s:
#         return ''

#     n = len(s)
#     res = ''
#     start = 0
#     max_cnt = 0
#     i = 0
#     while i < n:
#         while i < n - 1 and s[i] == s[i + 1]:
#             i += 1
#         cur_cnt = i - start + 1
#         if cur_cnt > max_cnt:
#             res = s[start]
#             max_cnt = cur_cnt
#         i += 1
#         start = i 
#     return res



def get_maxchar(s):
    # 这个模板的意义：固定了end 找最大的start在哪里
    start = 0
    max_lens = 0
    res = ''
    for end in range(len(s)):
        # 不符合条件往后移动start
        while s[end] != s[start]:
            start += 1
        # while出来是满足条件的，记录答案
        cur_lens = end - start + 1
        if cur_lens > max_lens:
            res = s[start]
            max_lens = cur_lens
    return res
        



s = 'aabcccdee'
print(get_maxchar(s))
