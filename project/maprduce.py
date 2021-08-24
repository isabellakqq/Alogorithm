'''
Return sends a specified value back to its caller whereas Yield can produce a sequence of values. 
We should use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory.
Yield are used in Python generators. A generator function is defined like a normal function, 
but whenever it needs to generate a value, it does so with the yield keyword rather than return. 
If the body of a def contains yield, the function automatically becomes a generator function.
'''
class NGram:
    def mapper(self, n, string):
        for i in range(len(string) - n + 1):
            yield string[i : i+n], 1
    
    def reducer(self, key, value):
        yield key, sum(value)
s = NGram()
n = 3
string = 'abcabcabcabcbbcabc'
# for k, v in s.mapper(n, string):
#     print(k, v)
for k, v in s.reducer(key='abc', value=[1, 2, 3]):
    print(k, v)