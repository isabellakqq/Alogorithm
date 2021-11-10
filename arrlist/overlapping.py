def meeting_planner(slotsA, slotsB, dur):

    i, j = 0, 0
    m, n = len(slotsA), len(slotsB)
    while i < m and j < n:
        
        start = max(slotsB[j][0], slotsA[i][0])
        print(start)
        end = min(slotsB[j][1], slotsA[i][1])
        print(end)
        overlapping = end - start
        if overlapping >= dur:
            return [start, start + dur]
        else:
            if slotsB[j][1] < slotsA[i][1]:
                j += 1
            else:
                i += 1
    return []
# slotsA = [[10, 50], [60, 120], [140, 210]]
# slotsB = [[0, 15], [60, 70]]
dur = 2
a = [[5,10]]
b = [[2,3],[5,7]]

res = meeting_planner(a, b, dur)
print(res)