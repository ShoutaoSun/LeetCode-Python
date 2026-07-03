'''
    普通数组 - 轮转数组
'''

class Solution:
    def rotate1(self, nums, k):
        result = [0] * len(nums)
        for i in range(len(nums)):
            result[(i + k) % len(nums)] = nums[i]
        return result

    def rotate(self, nums, k):  # 三次翻转
        nums.reverse()
        k = k % len(nums)

        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        
        return nums


# test
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(Solution.rotate(Solution, nums, k))