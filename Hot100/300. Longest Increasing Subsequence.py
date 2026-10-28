'''
    最长递增子序列
'''

class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n  # 每个元素自己就是一个长度为 1 的子序列
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i] + 1)
        return max(dp)

# test
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(Solution.lengthOfLIS(Solution, nums))
