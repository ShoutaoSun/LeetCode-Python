'''
    只出现一次的数字
'''

class Solution:
    def singleNumber(self, nums):
        from functools import reduce
        return reduce(lambda x, y: x ^ y, nums)

# test
nums = [2, 2, 1]
print(Solution.singleNumber(Solution, nums))
