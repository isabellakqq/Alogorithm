'''
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
solution1:Insert new Interval into the sorted position, call MergeIntervals function
soulution2:Find the overlapping set and merge that range
Output: left + merged(overlappings) + right
'''

def insertIntervals(intervals, newInterval):
  index = len(intervals)
  for i in range(len(intervals)):
    if intervals[i][1] < newInterval[0]:
      index = i
      break
  intervals.insert(index, newInterval)
  res = []
  for interval in sorted(intervals):
      if not res or interval[0] > res[-1][1]:
          res.append(interval)
      else:
          res[-1][1] = max(res[-1][1], interval[1])
  return res

t = insertIntervals([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
print(t)
  
    

