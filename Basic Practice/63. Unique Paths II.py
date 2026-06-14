'''
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The testcases are generated so that the answer will be less than or equal to 2 * 10^9.
'''

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)  # rows
        n = len(obstacleGrid[0])  # cols
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            else:
                dp[i][0] = 1

        for k in range(n):
            if obstacleGrid[0][k] == 1:
                break
            else:
                dp[0][k] = 1

        for p in range(1, m):
            for q in range(1, n):
                if obstacleGrid[p][q] == 1:
                    dp[p][q] = 0
                else:
                    dp[p][q] = dp[p-1][q] + dp[p][q-1]

        return dp[m-1][n-1]

# test
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(Solution.uniquePathsWithObstacles(Solution(), obstacleGrid))