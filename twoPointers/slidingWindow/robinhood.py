
'''
/*

We are working on a security system for a badged-access room in our company's building.

We want to find employees who badged into our secured room unusually often. 
We have an unordered list of names and entry times over a single day. Access times are given as numbers up to four digits in length using 24-hour time, 
such as "800" or "2250".

Write a function that finds anyone who badged into the room three or more times in a one-hour period. <= 60, times >= 3
Your function should return each of the employees who fit that criteria, plus the times that they badged in during the one-hour period.
 If there are multiple one-hour periods where this was true for an employee, just return the earliest one for that employee.

badge_times = [
  ["Paul",      "1355"], ["Jennifer",  "1910"], ["Jose",    "835"],
  ["Jose",       "830"], ["Paul",      "1315"], ["Chloe",     "0"],
  ["Chloe",     "1910"], ["Jose",      "1615"], ["Jose",   "1640"],
  ["Paul",      "1405"], ["Jose",       "855"], ["Jose",    "930"],
  ["Jose",       "915"], ["Jose",       "730"], ["Jose",    "940"],
  ["Jennifer",  "1335"], ["Jennifer",   "730"], ["Jose",   "1630"],
  ["Jennifer",     "5"], ["Chloe",     "1909"], ["Zhang",     "1"],
  ["Zhang",       "10"], ["Zhang",      "109"], ["Zhang",   "110"],
  ["Amos",         "1"], ["Amos",         "2"], ["Amos",    "400"],
  ["Amos",       "500"], ["Amos",       "503"], ["Amos",    "504"],
  ["Amos",       "601"], ["Amos",       "602"]];
1, 2, 3, 4, 5, 6
Expected output (in any order)
   Paul: 1315 1355 1405
   Jose: 830 835 855 915 930 
   Zhang: 10 109 110
   Amos: 500 503 504

*/
'''
import collections

def find_people(badge_times):
    d = collections.defaultdict(list)
    for name, time in badge_times:
        d[name].append(time)
    
    
    res = {}

    for k, v in d.items():
        if len(v) >= 3:
            collect_res(k, v, res)
    return res


def collect_res(k, v, res):
    v.sort(key = lambda x : int(x))
    i = 0
    n = len(v)
    j = 0
    while j < n:
        # invalid move i
        while int(v[j]) - int(v[i]) > 100:
            i += 1

        # valid move j get max 
        if j - i + 1 >= 3:
            while j < n and int(v[j]) - int(v[i]) <= 100:
                j += 1
            res[k] = v[i : j]
            break
        j += 1

    




#Jose': ['835', '830', '1615', '1640', '855', '930', '915', '730', '940', '1630'],#    

  
# def parse(s):
#     if len(s) <= 2:
#         return int(s)
#     if len(s) == 3:
#         return int(s[0]) * 60 + int(s[1:3])
#     if len(s) == 4:
#         return int(s[:2]) * 60 + int(s[2:4])


    

badge_times = [
  ["Paul",      "1355"], ["Jennifer",  "1910"], ["Jose",    "835"],
  ["Jose",       "830"], ["Paul",      "1315"], ["Chloe",     "0"],
  ["Chloe",     "1910"], ["Jose",      "1615"], ["Jose",   "1640"],
  ["Paul",      "1405"], ["Jose",       "855"], ["Jose",    "930"],
  ["Jose",       "915"], ["Jose",       "730"], ["Jose",    "940"],
  ["Jennifer",  "1335"], ["Jennifer",   "730"], ["Jose",   "1630"],
  ["Jennifer",     "5"], ["Chloe",     "1909"], ["Zhang",     "1"],
  ["Zhang",       "10"], ["Zhang",      "109"], ["Zhang",   "110"],
  ["Amos",         "1"], ["Amos",         "2"], ["Amos",    "400"],
  ["Amos",       "500"], ["Amos",       "503"], ["Amos",    "504"],
  ["Amos",       "601"], ["Amos",       "602"],
]
print(find_people(badge_times))

