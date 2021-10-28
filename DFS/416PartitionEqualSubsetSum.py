from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # corner case
        # time: t *n
        # space: t
        
        total = sum(nums)
        
        if total % 2 != 0:
            return False
        
        return self.dfs(nums, 0, total // 2, {})
    
    
    def dfs(self, nums, index, remain, memo):
        
        if remain in memo:
            return memo[remain]
        
        if remain < 0:
            return False
        
        # find subset 
        if remain == 0:
            return True
        
        res = False
        
        for i in range(index, len(nums)):
            if self.dfs(nums, i + 1, remain - nums[i], memo):
                res = True
                break
                
        # record before return 
        memo[remain] = res
        return res
            
        