'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
'''

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        i, j, sum = 0, 0, 0
        l, result = len(nums), float('inf')
        while j < l:
            sum += nums[j]
            while sum >= target:
                subl = j - i + 1
                result = min(result, subl)
                sum -= nums[i]
                i += 1
            j += 1
        return result if result != float('inf') else 0

# test
target = 7
nums = [2, 3, 1, 2, 4, 3]
print(Solution.minSubArrayLen(Solution(), target, nums))