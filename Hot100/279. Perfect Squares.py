'''
    完全平方数
'''

class Solution:
    def numSquares(self, n):
        dp = [i for i in range(n + 1)]
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]

# test
n = 12
print(Solution.numSquares(Solution, n))
