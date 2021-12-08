'''
Question

Let's assume we have data about start and end time of Uber trips, e.g.
Trip 1: Start: 0, End: 5
Trip 2: Start: 1, End: 2
Trip 3: Start: 3, End: 7

Based on this input we want to print number of trips in progress per time slot:
[0, 1] -> 1
[1, 2] -> 2
[2, 3] -> 1
[3, 5] -> 2
[5, 7] -> 1



[[0, 5],[1, 2],[3, 7]]
[0, 5]
[0, 1] = 1


(0, 1), (1, 1),(1, 1), (2, -1) (2, -1), (3, 1), (5, -1), (7, 1)

start 一样的时候往后移动一下

for i in range(n):



[(0, 1, 1), (1, 2, 2), (2, 3, 1), (3, 5, 2), (5, 7, 1)]




'''
def cnt_intervals(trips):
    arr = []
    for s, e in trips:
        arr.append((s, 1))
        arr.append((e, -1))
    arr.sort()
    print(arr)
    pre_start = arr[0][0]
    cnt = 1
    res = []
    i = 1
    for i in range(1, len(arr)):
        
        if arr[i][0] == arr[i - 1][0]:
            continue
            

        else:
            res.append((pre_start, arr[i][0], cnt))
            pre_start = arr[i][0]
      
        cnt += arr[i][1]
    return res
trips = [[0, 5],[1, 2],[3, 7]]
print(cnt_intervals(trips))

        




