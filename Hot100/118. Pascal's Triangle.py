'''
    杨辉三角
'''

class Solution:
    def generate(self, numRows):
        dp = [[1] * (numRow + 1) for numRow in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        return dp

# test
numRows = 5
print(Solution.generate(Solution, numRows))
        