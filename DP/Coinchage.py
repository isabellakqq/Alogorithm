from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        [1,2,5] 11
        i :amount we want to make up
        dp[i] stores the fewest the amount of coins to make up the amounti
        i     0    1    2  3   4   5   6   7   8   9   10  11
        dp[i] 0    1    1  2   2   1   2   2   3   3    2   3
        Induction Rule:
            for coin in coins: dp[i] = min(dp[i], dp[i - coin] + 1)
        time: amount*N
        space:amonut
        '''
        
        dp = [amount + 1] * (amount + 1)
        #初始化amount + 1 是应为要dp[0] = 0:凑齐0元需要的最少coin数量是0
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != amount + 1 else -1
        