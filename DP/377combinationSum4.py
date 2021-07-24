from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        '''
        [1,2,5] 11
        i :amount we want to make up
        dp[i] stores the fewest the amount of coins to make up the amounti
        i     0    1    2  3   4 
        dp[i] 1    1    2  2   2 
        Induction Rule:
            for coin in coins: dp[i] = min(dp[i], dp[i - coin] + 1)
        time: amount*N
        space:amonut
        '''
        nums.sort()
        dp = [0]*(target + 1)
        dp[0] = 1
        for i in range(target + 1):
            for num in nums:
                if i - num < 0:
                    break
                dp[i] += dp[i - num]
        return dp[target] 
        
