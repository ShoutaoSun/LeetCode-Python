class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = (amount + 1) * [0]
        dp[0] = 1

        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        return dp[amount]

# test
amount = 5
coins = [1, 2, 5]
print(Solution.change(Solution(), amount, coins))