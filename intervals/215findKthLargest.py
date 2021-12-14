'''
fb
min_heap 更好，因为datastream 实时更新top k online algorithm
数据很大的时候
n*logk
arr = [9, 7, 4, 5, 8] top k 
1, 4 clarify
1: size 是不是很大能不能can it fit in the memo(data stream) online给你的
2: arr  -> query 是不是high frequent的 今天top3 明天top5， query heavily
3: heavily 就sort一下， 
4: top k要sort 好的还是不需要：topkth or 前k 大如果是一个list 是不是需要inorder ：any order or deceding order
5: duplicate的元素会不会特别多（quick_select 就 n方的时间复杂度）------ min_heap 或者 modified quick_select(partition, three way patition-------ipppppppj------- 如果k在i， j中间返回nums[k])
6:k nums[:k].sort()
7: quick_select average O(N)time and o(1) idealy we will remove half of the arr every time so it is n + 1/2n + n/4 +.... = 2N - 1 
8:手动跑

'''
def findKthLargest(arr, k):
    if not arr:
        return -1

    return quick_select(arr, k-1)

def quick_select(arr, k):
    # [9, 7, 8, 5, 4]
    left = 0 # left = 0, 0,  2
    right = len(arr) - 1 # right = 4, 3, 3
    while left <= right:
        '''
        [9, 7, 8, 5, 4]
                       i
                  j

        [9, 8, 7, 5, 4]
               i
            j

        [9, 8, 7, 5, 4]
                  i
            j
                # k is inplace return arr[k]

        '''
        pivot = arr[(left + right) // 2]  # pivot = 8
        i = left # i = 0 , 0
        j = right # j = 4,  3
        while i <= j:
            if arr[i] > pivot:
                i += 1

            elif arr[j] < pivot:
                j -= 1
            # 为什么不能 i, j都移动？
            #i 的物理意义是  i 的左边不包括 i 都 > pivot
            #j 的物理意义是  j 的右边不包括 j 都 < pivot
            #保证交换的时候一定是不满足前面两个if --- else
            else:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        print(arr)
        if k >= i:
            left = i
        elif k <= j:
            right = j
        # 所以 i < k < j才能确定 arr[k] == pivot 
        else:
            # 最后一次的pivot == arr[k]
            return arr[k]
        
arr = [9, 7, 4, 5, 8]
print(findKthLargest(arr, 3))

