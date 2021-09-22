a = [1, 9, 0, 21, 2, 8, 9, 2]
cnt = [0] * 24
def count_sort(arr):
    for n in arr:
        cnt[n] += 1
    k = 0
    for i in range(24):
        for _ in range(cnt[i]):
            a[k] = i
            k += 1
    return arr
print(count_sort(a))