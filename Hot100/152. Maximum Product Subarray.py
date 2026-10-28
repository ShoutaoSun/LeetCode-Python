'''
    乘积最大子数组
'''

class Solution:
    def maxProduct(self, nums):
        # 需要维护两个数组：正数的最大乘积，负数的最小乘积（负负得正）
        ans = float('-inf')
        f_max = f_min = 1
        for i in range(len(nums)):
            # 同时更新
            f_max, f_min = max(nums[i], f_max * nums[i], f_min * nums[i]), \
                           min(nums[i], f_max * nums[i], f_min * nums[i])
            ans = max(ans, f_max)
        return ans
    