A = [2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5]
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

print(solution(A))
print("A" * 3)