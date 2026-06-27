'''
    哈希 - 两数之和
'''

class Solution:
    def twoSum(self, nums, target):
        hash_table = {}  # 创建哈希表用于实现快速检索

        for i, num in enumerate(nums):
            tmp = target - num

            if tmp in hash_table:
                return [hash_table[tmp], i]
            
            hash_table[num] = i

# test
nums = [3, 3]
target = 6
print(Solution.twoSum(Solution, nums, target))