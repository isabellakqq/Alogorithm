'''
Three Rules of Recursion
• Every (valid) input must have a case (either recursive or base)
• There must be a base case that makes no recursive calls
• The recursive case must make the problem simpler and make forward progress to the base case
Every recursive algorithm involves at least 2 cases:
– base case: A simple occurrence that can be answered directly
– recursive case: A more complex occurrence of the problem that cannot be directly answered, but can instead be described in terms of smaller occurrences of the same problem
– Key idea: In a recursive piece of code, you handle a small part of the overall task yourself (usually the work involves modifying the results of the smaller problems), then make a recursive call to handle the rest.

'''
def mystery(n):
    if n < 10:
        return 10*n + n
    a = mystery(n // 10)
    b = mystery(n % 10)
    return a * 100 + b
print(mystery(348))