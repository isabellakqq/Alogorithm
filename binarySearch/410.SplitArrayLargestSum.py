from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        '''
        Input: nums = [7,2,5,10,8], m = 2
        Output: 18
        how to find search range
        binary search element is sorted 
        min_pieces = 1    ------- max_sub_sum = sum(nums)
        max_pieces = n    ------- min_sub_sum = max(nums)
        so the search range is : max(nums)  to sum(nums)
        
        upper limit is m
        
        is pieces > m:
            left = mid + 1
            
        else: 
            right = mid
        '''
        if len(nums) == 1:
            return nums[0]
        
        l = max(nums)
        r = sum(nums)
        
        while l < r:
            mid = (l + r) // 2
            pieces = self.get_pieces(nums, mid)
            
            if pieces > m:
                l = mid + 1
                
            else:
                r = mid 
        return l

    def get_pieces(self, nums, target):
        cur = 0
        p = 1
        
        for num in nums:
            
            if cur + num > target:
                cur = num
                p += 1
                
            else:
                cur += num
        return p
                
        
            