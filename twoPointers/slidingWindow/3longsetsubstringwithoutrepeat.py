class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
   
        clarify:
        compose all english letter?
        Without loss of generality then I will assum that all input are  lower case english leterrs
        for this problem use hash map
        key: ch
        value: freq
        then I will use two pointer sliding window
        start: the begain of valid sliding window
        end: the furthest we can reach from the start index
        if end index increse the coresponding start index will not decrease so the time complexity will be O(n)
        I can go through an example if you want

        solution:
                 use two pointer to carry sliding window
        the smallest possible——start pointer of window   
        end the end of valid window 
        for loop or end < len(len(s))
        while not valid shrink the window and deal with the hashset or hashmap
        for end_index scan whole nums
            while  start 以end为结尾满足条件的Longest Substring Without Repeating Characters的起点
        '''
        seen = set()
        start = 0
        res = 0
        for end in range(len(s)):
            while s[end] in seen:
                seen.remove(s[start])
                start += 1
               
            res = max(res, end - start + 1)
            
            seen.add(s[end])
            
        return res
                
            
                
            