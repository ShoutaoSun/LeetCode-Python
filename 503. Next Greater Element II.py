'''
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
'''

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [-1] * len(nums)
        stack = []

        for i in range(len(nums) * 2):
            while (len(stack)!= 0 and nums[i%len(nums)] > nums[stack[-1]]):
                result[stack[-1]] = nums[i%len(nums)]
                stack.pop()
            stack.append(i%len(nums))
        
        return result

# test
nums = [1, 2, 1]
print(Solution.nextGreaterElements(Solution(), nums))