# s = 'i love yahoo'  
#  -----'yahoo love i'
# primitive solution: stack time o(n) n lens string, space: 0(n)
# def reverse(s):
#     stack = []
#     res = ''
#     for word in s.split(' '):
#         stack.append(word)
#     while stack:
#         res += ' ' + stack.pop()
#     return res
# print(reverse(s))
                                      
# i evol oohay
class Solution:
    '''
    reverse every wors
    reverse the whole sentence
    O(N) 2*n
    can not slicing it is deep copy will not change the original list
    '''
    def reverse(self, s):
        i = 0
        j = 0
        while j < len(s):
            while j < len(s) and s[j] != ' ':
                j += 1
            self.swap(s, i, j - 1)
            j += 1
            i = j
        self.swap(s, 0, len(s) - 1)
        return s

    def swap(self, l, i, j):
        while i < j:
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1
        
            
letters = ['i', ' ', 'l', 'o', 'v', 'e', ' ', 'y', 'a', 'h', 'o', 'o']    
test = Solution()
res = test.reverse(letters)
print(res)
    

    

