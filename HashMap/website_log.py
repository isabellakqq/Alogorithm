'''
Input: 
- (2021-09-16 23:40, 5) 41 36 37 38
- (2021-09-16 23:41, 3)  42-43-44
- (2021-09-16 23:58, 5)  59/  2021-09-17 00:00 4
- (2021-09-17 00:20, 4)21 22 23 24
- (2021-09-16 23:41, 3) <- duplicate ignore
- (2021-09-17 00:27, 5) 

first half hour: 0-29 = 00
second half hour: 30-59 = 30

Output:
{ 
   (2021-09-16 23:30, 4+3+1=8)
   (2021-09-17 00:00, 4+4+2=10)
   (2021-09-17 00:30, 3)
}

Constraints:
1. input may be out of order but generally in order
2. input may contain duplicates, but no overlaps.  ignore duplicates
3. input time elapsed <= 5 > 0

Requirements:
program to solve this problem

my solution: {key is 'yyyy-mm-dd+time' : value(lapse, list}
e.g 2021-09-16 23:34, 4  {2021-09-16 23:30 : 4 }
    2021-09-16 23:41, 3  {2021-09-16 23:30 : 7 }
    2021-09-16 23:58, 5  {2021-09-16 23:30 : 8 } 
    2021-09-17 00:20, 4  {2021-09-17 00:00 : 4 }
    2021-09-17 00:20, 4  {2021-09-17 00:00:  8 )}
step 1: define input date type
setp2 : get key and startTime from input
step3 : if key in map: lapselist = map[key] 
        hh, mm = startTime.split(':')
        index = int(mm) + 1 
        for _ in range(lapse):
            if not lapselist[index]:
                lapselist[index] = 1
                index += 1
            if index > 59:
                index %= 59
date to int 
int to date  
'''
from typing import DefaultDict


class Log:
    def __init__(self) -> None:
        self.map = DefaultDict(list)
    
    def put(self, timeStamp, lapse):
        key1, key2, lapse_list = helper(timeStamp, lapse)
        if ky1:
            self.map[key1] += sum(lapse_list[:30])
        if key2:
            self.map[key2] += sum(lapse_list[30:])
    def _helper(timeStamp, lapse):
        timeStamp = [0] * 60
        
        for i in range(lapse):
            index = startTime + 1
            if index > 59:
                change(key1)
                index %= 60
                timeStamp[index] += 1
        if 29 < mins + lapse < 59:
            key2 = yy + hh + '30'
        elif 0 <= mins + lapse <= 29:
            key1 = yy + hh + '00'


