'''
    在排序数组中查找元素的第一个和最后一个位置
'''

class Solution:
    def lower_bound(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def searchRange(self, nums, target):
        start = self.lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        # 若 start 存在，那么 end 必定存在
        end = self.lower_bound(nums, target + 1) - 1
        return [start, end]

# test
nums = [5,7,7,8,8,10]
target = 8
print(Solution().searchRange(nums, target))
        