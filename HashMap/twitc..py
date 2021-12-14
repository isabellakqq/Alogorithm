'''
['twitch', 'hello', 'Isa','twitch', 'hello', 'twitch']


input: list of string
ouput: ['twitch' : 3]
        ['hello' : 2]
        ['Isa' : 1]



'''

import collections


def get_freq(arr):
    if not arr:
        return None
    
    cnt = collections.defaultdict(int)

    for word in arr:
        cnt[word] += 1


    # reverse hashmapping
    d = collections.defaultdict(list)
    for k, v in cnt.items():
        d[v].append(k)

    max_cnt = max(cnt.values())
    res = []
    for i in range(max_cnt, -1, -1):
        if i in d:
            for w in d[i]:
                res.append((w, i))

    return res

arr = ['twitch', 'hello', 'Isa','twitch', 'hello', 'twitch', 'Isa']

print(get_freq(arr))

        