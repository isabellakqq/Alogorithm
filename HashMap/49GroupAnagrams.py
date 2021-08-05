class Solution:
    #time:nlogl(sort(ch)是llogl)
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = collections.defaultdict(list)
#         for s in strs:
#             res[tuple(sorted(s))].append(s)
#             print(res)
#         return res.values()
    #优化的时间复杂度：nl（就是不sort而是26个字母减ord('a')
    def groupAnagrams(self, strs):
        d = {}
        if not strs:
            return None
        for s in strs:
            reg = s
            new = ''.join(sorted(s))
            if new in d:
                d[new].append(reg)
            else:
                d[new] = [reg]
        return d.values()
            
        
        # res = collections.defaultdict(list)
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     res[tuple(count)].append(s)
        # return res.values()