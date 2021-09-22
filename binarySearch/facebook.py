def find_unique(arr):
    i = 0
    cnt = 0
    while i < len(arr):
        cnt += 1
        i = bs(arr, i)
    return cnt 

def bs(arr, i):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2