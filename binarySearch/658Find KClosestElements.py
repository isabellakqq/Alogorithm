import bisect
def findClosestelement(arr, k, x):
    index = bisect.bisect_right(arr, x)
    left = index - 1
    right = index
    for _ in range(k):
        if is_left_closer(arr, left, right, x):
            left -= 1
        else:
            right += 1
    return arr[left + 1 : right]

def is_left_closer(arr, left, right, x):
    if right >= len(arr):
        return True
    if left < 0:
        return False
    return abs(arr[left] - x) <= abs(arr[right] - x)

print(findClosestelement([1, 2, 3, 4, 5], 2, 0))
# print(bisect.bisect([1, 2, 3, 3, 5], 1))

