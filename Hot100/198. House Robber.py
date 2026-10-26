'''
    打家劫舍
'''

class Solution:
    def rob(self, nums):
        if not nums:
            return 0

        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[n - 1]

# test
nums = [1, 3, 1]
print(Solution.rob(Solution, nums))
