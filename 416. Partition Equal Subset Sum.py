'''
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

Example:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
'''

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2:
            return False
        
        target = sum(nums) / 2
        dp = [0] * (target + 1)

        for i in nums:
            for j in range(target, i - 1, -1):
                dp[j] = max(dp[j], dp[j - i] + i)

        if dp[target] == target:
            return True
        else:
            return False 

# test
nums = [1, 5, 11, 5]
print(Solution.canPartition(Solution(), nums))   