class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = (amount + 1) * [float('inf')]  # 将非零下标值设为无穷大
        dp[0] = 0

        for coin in coins:
            for j in range(coin, amount + 1):
                if j - coin != float('inf'):
                    dp[j] = min(dp[j], dp[j - coin] + 1)
            
        if dp[amount] == float('inf'):
            return -1
        
        return dp[amount]

# test
coins = [1, 2, 5]
amount = 11
print(Solution.coinChange(Solution(), coins, amount))