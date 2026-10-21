'''
    搜索旋转排序数组
'''

class Solution:
    def search(self, nums, target):
        n = len(nums)

        # 找旋转点
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left

        # 确定 target 在哪一段
        if pivot == 0:
            lo, hi = 0, n - 1
        elif target >= nums[0]:
            lo, hi = 0, pivot - 1      # 左段
        else:
            lo, hi = pivot, n - 1      # 右段

        # 普通二分
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
    