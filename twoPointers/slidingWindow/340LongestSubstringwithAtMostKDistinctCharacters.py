'''
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
'''
import collections
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        '''
        "eceba"
        for-----
            while不满足条件：
                deal with hashmap
                start + =1
            打擂台记录答案
        '''
        fre = collections.defaultdict(int)
        n = len(s)
        res = 0
        # 易错1定义start
        start = 0
        
        for end in range(n):
            fre[s[end]] += 1
            while len(fre) > k:
                fre[s[start]] -= 1
                
                if fre[s[start]] == 0:
                    del fre[s[start]]
                # 易错2: 忘记移动start
                start += 1
                    
            res = max(res, end - start + 1)
        
        return res
        