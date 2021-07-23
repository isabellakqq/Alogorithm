from typing import List


phone = {
                 '2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']
}
        
class Solution:
    '''
    clarify:
    assumption:
    result:dfs + backtraking to generate all possible combinations,
    recursion tree
            
        /              |            \
      a                b             c
  /   |   \        /   |   \     /   |   \  
  d    e   f       d    e   f
  d    e   f       d    e   f
  ad   ae   af
        
    test 
    time:O(4**N*N) where N is the length of digits
    space(N)
    '''
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        self.dfs(digits, 0, [], res)
        return res
    def dfs(self, digits, start, combination, res):
        if start == len(digits):
            res.append(''.join(combination))
            return 
       
        for ch in phone[digits[start]]:
            combination.append(ch)
            self.dfs(digits, start + 1, combination, res)
            combination.pop()

