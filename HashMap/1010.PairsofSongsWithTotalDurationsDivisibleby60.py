from collections import defaultdict
from typing import List
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        #same with "two sum"用dict记录remainders
        #time：o(n), space:o(1)
        d = defaultdict(int)
        res = 0
        for song in time:
            if song % 60 == 0:
                res += d[0]
            else:
                res += d[60 - song % 60]
            d[song % 60] += 1
        return res
        