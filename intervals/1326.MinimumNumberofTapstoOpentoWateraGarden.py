from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        arr = [0] * (n + 1)
        for i, r in enumerate(ranges):
            left = max(0, i - r)
            right = min(n, i + r)
            arr[left] = max(arr[left], right - left)
            
        left_most = 0
        res = 0
        end = 0
  
        # jump games2
        for start in range(n + 1):
            left_most = max(left_most, arr[start] + start)
            
            if end == start:
                res += 1
                end = left_most
                if end >= n:
                    return res
                
        return -1
            
            