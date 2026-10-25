'''
    买卖股票的最佳时机
'''

class Solution(object):
    def maxProfit(self, prices):
        cur = ans = 0
        if len(prices) <= 1:
            return ans

        for i in range(1, len(prices)):
            reward = prices[i] - prices[i - 1]
            cur = max(reward, cur + reward)
            ans = max(ans, cur)

        return ans
    