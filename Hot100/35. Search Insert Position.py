'''
    搜索插入位置
'''

class Solution:
    def searchInsert(self, nums, target):  # 二分查找
        left, right = 0, len(nums) - 1
        while left <= right:  # 区间不为空
            # 循环不变量
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

# test
nums = [1, 3, 5, 6]
target = 5
print(Solution.searchInsert(Solution, nums, target))
