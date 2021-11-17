import collections

def find_people(badge_times):
    arr = [(parse(time), name) for name, time in badge_times]
    arr.sort()
    n = len(arr)
    res = collections.defaultdict(list)
    start = 0
    d = collections.defaultdict(collections.deque)
    d[arr[0][1]].append(arr[0][0])
    seen = set()
    i = 1
    while i < n:
        # 满足条件
        while i < n and arr[i][0] - arr[start][0] <= 60:
            if arr[i][1] not in seen:
                d[arr[i][1]].append(arr[i][0])
            i += 1
        #  find a valid sliding window   i 移动多了1
        for k, v in d.items():
            if k not in seen and len(v) >= 3:
                res[k] = [parse_back(num) for num in v]
                seen.add(k)
        # 不满足条件移动start
        while i < n and arr[i][0] - arr[start][0] > 60:
            if arr[start][1] in seen:
                start += 1
                continue
            if len(d[arr[start][1]]) == 0:
                del d[arr[start][1]]
            else:
                d[arr[start][1]].popleft()
            start += 1
    return res
def parse(s):
    if len(s) <= 2:
        return int(s)
    if len(s) == 3:
        return int(s[0]) * 60 + int(s[1:3])
    if len(s) == 4:
        return int(s[:2]) * 60 + int(s[2:4])
def parse_back(num):
    if num < 60:
        return str(num)
    else:
        hh = str(num // 60)
        mm = str(num % 60)
        if len(mm) == 1:
            mm = '0' + mm
        return hh + mm

    

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
'''
/*

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

*/
'''
