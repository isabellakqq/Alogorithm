from typing import List
import math

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        '''
        n = 12 => dfs 2 - int(sqrt(12))      try 2, 3
        [[2,6],[3,4],[2,2,3]]
        
        level1
        n = 12  start = 2 path = [2,] 
        level2
        n = 6   start = 2  res = [[2, 6]] path = [2, 2]
        level3
        n = 3   start = 2 res = [[2, 6], [2, 2, 3]], path = [2]
        level4  
        start = 3 res = [[2,6], [ 2,2,3]], path = [3]
        level5
        s = 3.   res = [[2,6], [ 2,2,3], [3, 4]] path = []
        每次除一个2～math.sqrt(n) 之间能整除的数字。
        每次递归进来之后，只要path不是空，都是能被整除的解，所以直接加到result。
        math.sqrt(n) 很巧妙，会保证8只会被分解成2，2，2 和 2，4，而不会被分解成 4，2。
    
        
        
                n = 12
2       [2,6] /   [3, 4]  \      
           n =6           4  
2 [2,2,3]   /                         
        n = 3        
 
        '''
        if n < 4:
            return []
        res = []
        self.dfs(n, 2, [], res)
        return res
    def dfs(self, n, start, path, res):
        if path:
            res.append(path + [n])
        for i in range(start, int(math.sqrt(n)) + 1):
            if n % i == 0:
                path.append(i)
                self.dfs(n//i, i, path, res)
                path.pop()
  
            
            
            
            
        
        
    