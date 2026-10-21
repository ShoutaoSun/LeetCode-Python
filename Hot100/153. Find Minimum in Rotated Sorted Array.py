'''
    寻找旋转排序数组中的最小值
'''

class Solution:
    def findMin(self, nums):
        n = len(nums)
        
        # 找旋转点
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

# test
nums = [3, 4, 5, 1, 2]
print(Solution.findMin(Solution, nums))
