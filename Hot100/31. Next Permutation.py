'''
    下一个排列
'''

class Solution:
    def nextPermutation(self, nums):
        n = len(nums)

        # 第一步，从右到左找到第一个小于 nums[i + 1] 的数 nums[i]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 如果找到了，进入第二步；否则跳过第二步，反转整个数组
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # 第三步，反转 nums[i+1:]
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
        