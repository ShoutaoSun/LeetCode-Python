class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], prices[i] + dp[i][0])
            
        return dp[len(prices) - 1][1]
        
# test
prices = [7, 1, 5, 3, 6, 4]
print(Solution.maxProfit(Solution(), prices))