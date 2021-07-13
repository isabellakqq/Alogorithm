class Solution:
    def removeDuplicates(self, s: str) -> str:
        '''
        "abbaca"
        stack: [a]
        ab    [a,b]
        abb   [a]
        abba  []
        abbac [c]
        abbac [ca]
        '''
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
            