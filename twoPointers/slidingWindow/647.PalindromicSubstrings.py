
'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
'''
def countSubstrings(self, s: str) -> int:
    '''
    枚举每个palindrom的中心点
    time:O(N^2)
    '''
    res = 0
    for i in range(len(s)):
        #odd  a/bab/cbabc
        res += self.count_pali(s, i, i)
        #even aa/aabb/aabbcc
        res += self.count_pali(s, i, i + 1)
        
    return res


def count_pali(self, s, left, right):
    res = 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        res += 1
        left -= 1
        right += 1
        
    return res
            
        