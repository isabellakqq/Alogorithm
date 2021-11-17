from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            
            return [-1, -1]
        
        left = self.binary_search1(nums, target)
        
        right = self.binary_search2(nums, target)
        
        return [left, right]
    
    
    def binary_search1(self, nums, target):
        
        left, right = 0, len(nums) - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                res = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
                
            else:
                right = mid - 1
                
        return res
    
    def binary_search2(self, nums, target):
        
        left, right = 0, len(nums) - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            # if nums[mid] == target:
            #     res = mid
            #     left = mid + 1
                
            if nums[mid] <= target:
                res = mid
                left = mid + 1
                
            else:
                right = mid - 1
                
        return res