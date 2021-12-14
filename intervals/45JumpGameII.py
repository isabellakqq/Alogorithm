from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        贪心：greedy
        [2,3,1,1,4]
             i
             ^
            end
                 ^
                 end
                
        '''
        if not nums or len(nums) == 1:
            return 0
        right_most = 0
        start = 0
        end = 0
        steps = 0
        for start in range(len(nums)):
            right_most = max(right_most, start + nums[start])
            if start == end:
                end = right_most
                steps += 1
            if end >= len(nums) - 1:
                return steps
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        [2,3,1,1,4]
             ^
             end
                  ^
                  f
        
        '''
        if len(nums) <= 1:
            return True
        end = 0
        furthest = 0
        for start in range(len(nums)):
            furthest = max(furthest, start + nums[start])
            if start == end:
                end = furthest
            if end >= len(nums) - 1:
                return True
        return False   