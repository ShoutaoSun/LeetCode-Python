'''
    爬楼梯
'''

class Solution:
    def climbStairs(self, n):
        dp = [0] * (n + 1)  # dp 数组初始化
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# test
n = 4
print(Solution.climbStairs(Solution, n))
