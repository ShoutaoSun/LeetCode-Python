class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for str in strs:
            x = sum(1 for c in str if c == "0")
            y = sum(1 for c in str if c == "1")
            for i in range(m, x - 1, -1):
                for j in range(n, y - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - x][j - y] + 1)

        return dp[m][n]

# test
strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
print(Solution.findMaxForm(Solution(), strs, m, n))