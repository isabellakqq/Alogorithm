from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        中心开花
         step1: find closeted-number
         steps2: 移动k步
        
        '''
        
        if not arr:
            return []
        
        mid_index = self.find_closest(arr, x)
        print(mid_index)
        
        start = mid_index - 1
        end = mid_index
        
        for _ in range(k):
            if self.is_left_closer(arr, x, start, end):
                start -= 1
            
            else:
                end += 1
        print([start + 1, end])
                
        return arr[start + 1 : end]
    
    def is_left_closer(self, arr, x, left, right):
        if left < 0:
            return False
        
        if right >= len(arr):
            return True
        
        return x - arr[left] <= arr[right] - x
           
    def find_closest(self, arr, target):
        left = 0
        right = len(arr) - 1
        min_dis = float('inf')
        while left <= right:
            mid = (left + right) // 2
            
#             if arr[mid] == target:
#                 return mid
            
            if abs(arr[mid] - target) < min_dis:
                res = mid
                min_dis = abs(arr[mid] - target)
                
            if arr[mid] > target:
                right = mid - 1
                
            else:
                left = mid + 1
                
        return res
                
        