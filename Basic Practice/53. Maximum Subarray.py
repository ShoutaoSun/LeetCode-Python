'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.
'''

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])

        return max(dp)

# test
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution.maxSubArray(Solution(), nums))