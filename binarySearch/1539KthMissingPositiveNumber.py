'''
[2,3,4,7,11]
5
find 5th missing num
小于答案的最大index
'''
def find_kth_missing(arr, k):
    left = 0
    right = len(arr) - 1
    res = -1
    while left <= right:
        # 二分答案 对0取整和向下取整
        # python 向下取整 int(3/2) 
        # java, c++ 对0取整： eg: left = -2, right = -1, （-1 -2） / 2 = -1    （-1-（-2））/ 2 + -2 = -2
        # a/b 向上取整： （a + b - 1) // b
        # mid = left + (right - left) // 2
        mid = (left + right) // 2
        cnt_missing = arr[mid] - mid - 1
        if cnt_missing < k:
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    # res in between  arr[left] and arr[right]
    # res = k + right + 1
    # res = left + 1
    #这里的-1表明所有的res都比k大所以应该单独判断下
    if res == -1:
        return k
    return arr[res] + k - (arr[res] - res - 1)


arr = [2,3,4,7,11]
test = find_kth_missing(arr, 5)
print(test)