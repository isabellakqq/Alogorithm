'''
1-3
 2--6
      8-10
        9-18
[[1, 6], [8, 18]]
'''
class Solution(object):
    def merge(self, intervals):
        res = []
        for interval in sorted(intervals):
            print(intervals)
            if not res or interval[0] > res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res
s = Solution()
ans = s.merge([[1,3],[2,6],[8,10],[8,18]])
print(ans)