def caculate(s):

    index = [0]

    return recursion(s, index)

def recursion(s, index):
    ch = s[index[0]]
    if ch == '(':
        index[0] += 1

        left = recursion(s, index)

        oper = s[index[0]]

        index[0] += 1
    
        right = recursion(s, index)

        index[0] += 1

        if oper == '+':
            return left + right

        else:
            return left * right
    else:
        index[0] += 1
        return int(ch)
s = '2+(3*4)'
print(caculate(s))
    
        