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
'''
10/10/2021
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        i,j k three way patition
        
        i: represents all element before i(excluding i) are 0
        j: represents all element before i(exluding j) are 1
        k: cur index to scan whole arr [i, k) are 1, [k, j] are element to be processing
        [0,0,1,1,2,2]
         0 1 2 3 4 5
             i
                  k
                j
        
        
        """
        i = 0
        j = len(nums) - 1
        k = 0
        
        while k <= j:
            
            if nums[k] == 0:
                nums[k], nums[i] = nums[i], nums[k]
                i += 1
                k += 1
            elif nums[k] == 1:
                k += 1
                
            else:
                nums[j], nums[k] = nums[k], nums[j]
                j -= 1
                
            
            
        
'''
        
        