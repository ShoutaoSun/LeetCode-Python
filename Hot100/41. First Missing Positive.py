'''
    普通数组 - 缺失的第一个正数
'''

class Solution:
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1

# test
nums = [-5]
print(Solution.firstMissingPositive(Solution, nums))