class Solution:
    def minCost(self, n: int, cuts):
        cuts.sort()
        cuts_list = [0, *cuts, n]
        print(n)
        m = len(cuts_list)
        dp = [[float('inf')] * m for _ in range(m)]
        for i in range(m):
            dp[i][i] = 0
            if i < m - 1:
                dp[i][i + 1] = 0
                
        for lens in range(3, m + 1):
            for i in range(m - lens + 1):
                j = i + lens - 1
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cuts_list[j] - cuts_list[i])
        return dp[0][m-1]
s = Solution()
cuts_list = [1,3,4,5]
print(s.minCost(7, cuts_list))