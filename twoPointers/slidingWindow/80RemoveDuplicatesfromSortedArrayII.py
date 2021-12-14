class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        [0,0,1,1,2,3,2,3,3]
        [0,0,1,1,1,1,2,3,3]
            
               i
               j
        invirant想清楚再写，用一样pattern
        
                    i elements in left to i are deduplicated(excluding i)
                          j cur index to scan nums
             if nums[j] != nums[i-2]  i += 1 j += 1
             nums[i] == nums[j] 
                  j
        只要nums[j] != nums[i-2] fu值 nums[i]
        相等移动 i, j
        '''
        
        
        # invariant sth that never change定理
        # nums[0:i] is sorted  nums[i -2] nums[i - 1] 
        n = len(nums)
        
        if n < 3:
            return n
        
        i = 2
        
        for j in range(2, n):
            if nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i += 1
                
        return i
        