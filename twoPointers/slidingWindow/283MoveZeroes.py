
def moveZeroes(self, nums) -> None:
    """
    同向双指针：搞清楚两个index的物理意义
    consistent and invariant
    Do not return anything, modify nums in-place instead.
    [0,1,0,3,12]
        i
        j
    i:all elemnts left to i (excluding i is > 0)
    j: cur index to processing 

    """
    n = len(nums)
    # if n < 2:
    #     return nums
    
    i = 0
    for j in range(n):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            
    return nums
        
        