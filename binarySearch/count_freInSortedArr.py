'''
count the total appearances of a number in a sorted array. ‍
‌‍‌‍‌‍‍‍‌‌‍‌‌‌‍‌‍‌‍比如
 [1, 2, 4, 5, 5, 5, 6], 
target = 5, 
then return 3.
soretd arr, we can bianynary search find first index and second index
模版1需要考虑corner
第一个大于等于和最后一个小于等于
二分都需要考虑corner case：
1: 数组越界  not arr: return ** processing 
2: 找不到符合条件的 需要post processing
3: 二分找的是满足某种条件的边界
'''
def cnt_freq(arr, target):
    # corner case processing
    if not arr:
        return 0
    first_index = binary_search1(arr, target)
    second_index = binary_search2(arr, target)
    print([first_index, second_index])
    if first_index == -1:
        return 0
    return second_index - first_index + 1

def binary_search1(arr, target):
    left = 0
    right = len(arr) - 1
    res = -1
    while left <= right:
        mid = (left + right) // 2
        # if arr[mid] == target:
        #     res = mid
        #     right = mid - 1

        if arr[mid] >= target:
            res = mid
            right = mid - 1

        else:
            left = mid + 1
    # post processing
    return res if arr[res] == target else -1
def binary_search2(arr, target):
    left = 0
    right = len(arr) - 1
    res = -1
    while left <= right:
        mid = (left + right) // 2
        # if arr[mid] == target:
        #     res = mid
        #     left = mid + 1

        if arr[mid] > target:
            right = mid - 1

        else:
            res = mid
            left = mid + 1

    return res if arr[res] == target else -1

    
   
  

arr = [1, 2, 4, 5, 5, 5, 5]
print(cnt_freq(arr, 5))

