def search_in_rotated(arr, target):
    if not arr:
        return -1

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid

        if arr[mid] < arr[left]:
            if arr[mid] < target <= arr[right]:
                left = mid + 1

            else:
                right = mid - 1

        else:
            if arr[left] <= target < arr[mid]:
                right = mid - 1

            else:
                left = mid + 1

    return -1

arr = [4, 6, 7, 2, 3]
print(search_in_rotated(arr, 2))