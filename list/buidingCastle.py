
'''
A = [2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5]
 
        /
    __
   /
--
find a peak and valley and start and end 
This problem is asking me to find how many hills and valleys in the input array . 
The condition for a hill is that its height is higher than its left and right borders, 
and the condition for a valley is that its height is smaller than its left and right borders. 
So we need to find out all possible pisitions satify either of these two conditions.
So I came up with 2 pointers to scan the array, and I use two pointers to check the two conditions.
Once the condition is true, I will increment my res by 1. I aslo need to address 2 corner cases: the begining index, 
and the end index. These 2 positions are automatically hill or valley as long as they have different height than their neighbors. 
So I can include these 2 corner cases together with my 2 conditions mentioned before.
'''

def solution(A):
    if not A:
        return 0
    
    i = 0
    j = 0
    
    res = 0
    while i < len(A):
        while j < len(A) - 1 and A[j] == A[j + 1]:
            j += 1
            
        if i == 0 or j == len(A) - 1 or A[i - 1] > A[j] and A[j] < A[j + 1] or A[i - 1] < A[j] and A[j] > A[j + 1]:
            res += 1
            
        
        j += 1
        i = j
        
    return res
A = [2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5]
print(solution(A))