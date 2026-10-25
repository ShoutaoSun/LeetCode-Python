'''
    数组中的第 K 个最大元素
'''

class Solution:
    def findKthLargest(self, nums, k):  # 三路划分，随机数选择
        import random
        def quick_select(nums, k):
            pivot = random.choice(nums)
            big, equal, small = [], [], []
            for num in nums:
                if num > pivot:
                    big.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    equal.append(num)

            if k <= len(big):
                return quick_select(big, k)
            if len(nums) - len(small) < k:
                return quick_select(small, k - len(nums) + len(small))
            return pivot
        return quick_select(nums, k)
        