class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        '''
        [a:2]
        
        '''
        stack = []
        if len(s) < k:
            return s
        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([ch, 1])
                #tuples are immutable. Convert to a list before processing.
        return ''.join(char * cnt for char, cnt in stack )