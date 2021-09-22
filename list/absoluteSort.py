def absoluteSort(arr):
    if not arr:
        return arr
    quickSort(arr, 0, len(arr) - 1)
    return arr

def quickSort(arr, left, right):
    if left >= right:
        return 
    pivot = arr[(left + right) // 2]
    i = left
    j = right
    while i <= j:
        while i <= j and is_smaller(arr[i], pivot):
            i += 1
        while i <= j and is_smaller(pivot, arr[j]):
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
    quickSort(arr, left, j)
    quickSort(arr, i, right)

def is_smaller(n1, n2):
    return abs(n1) < abs(n2) or abs(n1) == abs(n2) and n1 < n2

# import random
# def absSort(arr):
#     quick_sort_laioffer(arr, 0, len(arr) - 1)
#     return arr

# def quick_sort_laioffer(arr, start, end):
#     if start >= end:
#         return    
#     pivot_index = partition(arr, start, end)
#     quick_sort_laioffer(arr, start, pivot_index - 1)
#     quick_sort_laioffer(arr, pivot_index + 1, end) 

# def partition(arr, start, end): 
#     random_index = random.randint(start, end)
#     arr[random_index], arr[end] = arr[end], arr[random_index]
        
#     left, right = start, end - 1
#     pivot = arr[end]
#     while left <= right:
#         while left <= right and is_smaller(arr[left], pivot):
#             left += 1
#         while left <= right and not is_smaller(arr[right], pivot):
#             right -= 1
#         if left <= right:
#             arr[left], arr[right] = arr[right], arr[left]
#             left += 1
#             right -= 1
#     arr[left], arr[end] = arr[end], arr[left]
#     return left
    
# def is_smaller(a, b):
#     return abs(a) < abs(b) or abs(a) == abs(b) and a < b 
    
# arr = [4, 3, -2, -3, 0, 2, 1]    
# print(arr)
# print(absSort(arr))
# print(sorted(arr , key=lambda x: (abs(x), x)))          