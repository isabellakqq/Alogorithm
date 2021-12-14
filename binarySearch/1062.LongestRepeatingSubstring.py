def longestRepeatingSubstring(s: str) -> int:
        '''
        答案上二分
        hashset + binary search
        time: logn * l*(n - l) 
        '''
        l = 0
        r = len(s) - 1
        
        while l < r:
            mid = (l + r + 1) // 2
            
            if valid(s, mid):
                l = mid
                
            else:
                r = mid - 1
                
        return l
    
def valid(s, lens):
    
    seen = set()
    
    for i in range(len(s) - lens + 1):
        
        sub = s[i : i + lens]
        
        if sub in seen:
            return True
        seen.add(sub)
        
    return False
    