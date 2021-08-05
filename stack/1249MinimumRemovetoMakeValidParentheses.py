def minRemoveToMakeValid(self, s: str) -> str:
    s = list(s)
    stack = []
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        if ch == ')':
            if stack:
                stack.pop()
            else:
                s[i] = ''
    for index in stack:
        s[index] = ''
    return ''.join(s)