'''

We are working on a security system for a badged-access room in our company's building.

We want to find employees who badged into our secured room unusually often. 
We have an unordered list of names and entry times over a single day. Access times are given as numbers up to four digits in length using 24-hour time, 
such as "800" or "2250".

Write a function that finds anyone who badged into the room three or more times in a one-hour period. 
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
'''
import collections

def find_people(badge_times):
    d = collections.defaultdict(list)
    res = collections.defaultdict(list)
    # 每个人的时间抽出来： {key : name, value : list of time}
    for name, time in badge_times:
        d[name].append(time)
    # 排序取res
    for k, v in d.items():
        if len(v) >= 3:
            collect_valid(k, v, res)
    return res

def collect_valid(k, arr, res):
   #排序
    arr.sort(key = lambda x : int(x))
    start = 0
    n = len(arr)
    # slidingwindow一般求最长或者最短，固定end去找最大的start的，然后枚举所有index作为可能的end， 没有漏掉所有的可能性
    # update hashset/map
    for end in range(n):
        
        while parse(arr[end]) - parse(arr[start]) > 60:
            start += 1
        if end - start + 1 >= 3:
            # 满足条件找最长的最早的
            while end < n and parse(arr[end]) - parse(arr[start]) <= 60:
                end += 1
            res[k] = arr[start : end]
            return 

def parse(s):
    if len(s) <= 2:
        return int(s)
    if len(s) == 3:
        return int(s[0]) * 60 + int(s[1:3])
    if len(s) == 4:
        return int(s[:2]) * 60 + int(s[2:4])

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