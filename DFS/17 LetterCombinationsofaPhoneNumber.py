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
        res = []
        if not digits:
            return res
        PHONE = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        self.dfs(digits, 0, PHONE, [], res)
        return res
    
    def dfs(self, digits, index, PHONE, path, res):
        if index == len(digits):
            res.append(''.join(path))
            return 
        letters = PHONE[digits[index]]
        for i in range(len(letters)):
            path.append(letters[i])
            self.dfs(digits, index + 1, PHONE, path, res)
            path.pop()
            
            