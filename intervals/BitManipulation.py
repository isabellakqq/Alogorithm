'''
Concept

If we take XOR of zero and some bit, it will return that bit
a ^ a = 0
b ^ 0 = b
a^b^a = a^a^b = 0^b = b
'''
def find_single(l):
    a = 0
    for n in l:
        a ^= n
    return a
arr = [1,2,3,3,1]
print(find_single(arr))

def find_missing_number(A):
    missing_num = len(A)
    for i, n in enumerate(A):
        missing_num ^= i ^ n
    return missing_num
# arr2 = [1, 2, 3, 4]
# print(find_missing_number(arr2))
