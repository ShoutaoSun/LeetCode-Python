class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if abs(target) > sum(nums):  # 避免超大数
            return 0
            
        if (sum(nums) + target) % 2:
            return 0
        
        left = (sum(nums) + target) // 2
        dp = [0] * (left + 1)
        if len(dp) > 0:
            dp[0] = 1
        
        for num in nums:
            for j in range(left, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[left]
        
# test
nums = [1, 1, 1, 1, 1]
target = 3
print(Solution.findTargetSumWays(Solution(), nums, target))