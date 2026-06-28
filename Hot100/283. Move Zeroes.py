'''
    双指针 - 移动零
'''

class Solution:
    def moveZeroes(self, nums):
        j = 0  # 指向第一个零的位置

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return nums
    
# test
nums = [1, 0, 0, 2]
print(Solution.moveZeroes(Solution, nums))