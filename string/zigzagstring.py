def zigzag_coversion(s, numRows):
    if numRows == 1:
        return s
    res = [''] * numRows
    index, step = 0, 1
    
    for ch in s:
        res[index] += ch
        #index is 0 go Go in the forward direction 
            
        #tuch bottom of row go in the opposite direction index - 1
        if index == 0:
            step = 1
        if index == numRows - 1:
            step = -1
        
        index += step
    return ''.join(res)
s = "PAYPALISHIRING"
test = zigzag_coversion(s, 3)
print(test)