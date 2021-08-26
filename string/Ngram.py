'''
Challenge 1: N-grams

An N-gram is a sequence of N consecutive characters from a given word. For the word "pilot" there are three 3-grams: "pil", "ilo" and "lot". For a given set of words and an n-gram length Your task is to

• write a function that finds the n-gram that is the most frequent one among all the words
• print the result to the standard output (stdout)
• if there are multiple n-grams having the same maximum frequency please print the one that is the smallest lexicographically (the first one according to the dictionary sorting order)
Note that your function will receive the following arguments:

• text
    ○ which is a string containing words separated by whitespaces
• ngramLength
    ○ which is an integer value giving the length of the n-gram
Data constraints

• the length of the text string will not exceed 250,000 characters
• all words are alphanumeric (they contain only English letters a-z, A-Z and numbers 0-9)
Efficiency constraints

• your function is expected to print the result in less than 2 seconds
Example Input text: “aaaab a0a baaab c”

Output aaa ngramLength: 3

Explanation

For the input presented above the 3-grams sorted by frequency are:

• "aaa" with a frequency of 3
• "aab" with a frequency of 2
• "a0a" with a frequency of 1
• "baa" with a frequency of 1
'''


import collections
# from typing import DefaultDict
# def findNgram(s):
#     d = DefaultDict(int)
#     listOfs = s.split(' ') # O(N)
#     for s in listOfs: #O(N)
#         for i in range(len(s) - n + 1):# O(N)
#             d[s[i : i + n]] += 1
def getNgram(str, n):
    arr = str.split(' ')
    counts = collections.Counter()
    for word in arr:
        if len(word) >= n:
            rollingHash(word, n, counts)
        
    return max(counts.values())

def rollingHash(word, n, counts):
    base, mod = 31, 10000007
    power = 1
    hash_code = 0
    
    # h(abc)
    for i in range(n):
        hash_code = (base * hash_code + ord(word[i])) % mod
        power = (base * power) % mod
    
    counts[hash_code] += 1
    
    # rolling hash h(bcd) = 31 * h(abc) + d - 31^3 * a
    for i in range(1, len(word) - n + 1):
        hash_code = (base * hash_code + ord(word[i + n - 1]) - power * ord(word[i - 1])) % mod
        counts[hash_code] += 1 

s = "aaaab a0a baaab c"
print(getNgram(s, 3))