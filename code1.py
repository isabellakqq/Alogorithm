'''
Suppose we have some logs of request data in chronological order telling us 
when users have created, joined, or left Twitter Spaces. Here is a sample:

# action, space, user, timestamp
requests = [
    ["create", "xyz", "1", "1619916081"],
    ["join", "xyz", "2", "1619916681"], 
    ["create", "abc", "3", "1619916881"],
    ["leave", "xyz", "2", "1619920281"],
    ["join", "abc", "4", "1619920881"],
    ["create", "ghi", "5", "1619923999"],
    ["leave", "xyz", "1", "1619923881"],
    ["leave", "abc", "3", "1619927481"],
    ["leave", "abc", "4", "1619927481"],
    ["leave", "ghi", "5", "1619958001"]
]



For example, in the first row, user 1 creates space "xyz" at timestamp 
1619916081.

Write a method to find out how much total time was spent in each space, 
over all users.

'''