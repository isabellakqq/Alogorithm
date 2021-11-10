from typing import List

def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    quick sort pattern
    
    i: all number to the left-hand of side of i are all 0
    j: all number to the right-hand of side of j are all 2
    cur: current index
    all letter in [i, cur) are all 1
    unknow: [cur, j)
    [0,0,1,1,2,2]
        i
            cur
            j
    """
    i = 0
    j = len(nums) - 1
    cur = 0
    while cur <= j:
        if nums[cur] == 0:
            nums[cur], nums[i] = nums[i], nums[cur]
            i += 1
            cur += 1
        elif nums[cur] == 2:
            nums[cur], nums[j] = nums[j], nums[cur]
            j -= 1
        else:
            cur += 1
arr = [0, 1, 2, 1, 0, 2]
sortColors(arr)
print(arr)
            
        
        