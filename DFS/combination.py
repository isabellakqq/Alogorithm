'''
11:11

intervals lens = n
(2,5), (4,5), (5,7) 
[2, 3, 4, 5] [4, 5] [5, 6, 7]
4 - 1.         2 - 1.  3 - 1
res = []
path = [] "".join(path)
dfs (intervals, i, path, res)
['245', '255']

L: max interval length
N: num of intervals
n * 
number: "246", "248"
all numbers: 
input: postive list of intervals, overlap
output : list of str
[2, 3, 4, 5, 6, 7] = candinate

'''
def get_combinations(intervals):
    if not intervals:
        return []

    res = []
    
    dfs(intervals, 0, [], res, set())

    return res

def dfs(intervals, index, path, res, visited):
    # base case

    if index == len(intervals):
        res.append(path[:])
        return 
  
    # interval
    cand = intervals[index]
    # num
    for num in range(cand[0], cand[1] + 1):
        if num in visited:
            continue
        visited.add(num)
        path.append(num)
        dfs(intervals, index + 1, path, res, visited)
        path.pop()
        visited.remove(num)

arr = [[2,5], [4, 5], [5, 7]]
test = get_combinations(arr)
print(test)