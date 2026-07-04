'''
    普通数组 - 除了自身以外数组的乘积
'''

class Solution:
    def productExceptSelf(self, nums):
        answer = [1] * len(nums)
        for i in range(1, len(nums)):  # 计算左侧元素乘积
            answer[i] = answer[i - 1] * nums[i - 1]
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):  # 乘上右侧元素，计算总乘积
            answer[i] = answer[i] * right
            right = right * nums[i]

        return answer
    
# test
nums = [1, 2, 3, 4]
print(Solution.productExceptSelf(Solution, nums))