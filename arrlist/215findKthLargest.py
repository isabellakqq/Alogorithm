def findKthLargest(arr, k):
    if not arr:
        return -1

    return quick_select(arr, k-1)

def quick_select(arr, id):
    left = 0
    right = len(arr) - 1
    while left <= right:
       
        pivot = arr[(left + right) // 2]
        i = left
        j = right
        while i <= j:
            while i <= j and arr[i] > pivot:
                i += 1

            while i <= j and arr[j] < pivot:
                j -= 1
            # 为什么不能 i, j都移动？
            #i 的物理意义是  i 的左边不包括 i 都 > pivot
            #j 的物理意义是  j 的右边不包括 j 都 < pivot
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        print(arr)
        if id >= i:
            left = i
        elif id <= j:
            right = j
        # 所以 i < k < j才能确定 arr[k] == pivot 
        else:
            # 最后一次的pivot == arr[k]
            return pivot
        
arr = [9, 7, 4, 5, 8]
print(findKthLargest(arr, 1))

