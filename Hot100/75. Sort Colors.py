'''
    颜色分类
'''

class Solution:
    def sortColors(self, nums):  # 插入排序
        p0 = p1 = 0
        for i, x in enumerate(nums):
            nums[i] = 2  # 222222
            if x <= 1:  # 111122
                nums[p1] = 1
                p1 += 1
            if x == 0:  # 001122
                nums[p0] = 0
                p0 += 1
        return nums

# test
nums = [2, 0, 2, 1, 1, 0]
print(Solution.sortColors(Solution, nums))
