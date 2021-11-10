def get_insert_position(arr, target):
    '''
    [1,3,5,6] 2
    find first >= target 的index
    '''

    left = 0
    right = len(arr) - 1
    res = len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid

        if arr[mid] > target:
            res = mid
            right = mid - 1

        else:
            left = mid + 1

    return res

arr = [1,3,5,6]
print(get_insert_position(arr, 2))

