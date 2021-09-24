class Solution:
    def maxDistance(self, position, m: int) -> int:
        '''
        position = [1,2,3,4,7], m = 3
        l = 0       l = 1
        r = 6       r = mid - 1 = 3
        mid = 4     2
        cnt = 2 < 3 
        
        
        [79,74,57,22]
        [22, 57, 74, 79]
        
    
        '''
        position.sort()
        left = 0
        right = position[-1] - position[0]
        res = None
        while left <= right:
            mid = (left + right) // 2
            cnt = self.get_number(mid, position)
            if cnt >= m:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res
    
    def get_number(self,n, position):
        cur = position[0]
        cnt = 1
        for i in range(1, len(position)):
            if position[i] - cur >= n:
                cnt += 1
                cur = position[i]
        return cnt 
        
        
            
        