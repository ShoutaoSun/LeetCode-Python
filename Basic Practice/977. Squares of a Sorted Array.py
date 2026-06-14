'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
'''

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right, cur = 0, len(nums) - 1, len(nums) - 1
        res = [float('inf')] * len(nums)  # define the array
        while left <= right:
            if nums[left] ** 2 <= nums[right] ** 2:
                res[cur] = nums[right] ** 2
                right -= 1
            else:
                res[cur] = nums[left] ** 2
                left += 1
            cur -= 1
        return res
    
# test
nums = [-4, -1, 0, 3, 10]
print(Solution.sortedSquares(Solution(), nums))