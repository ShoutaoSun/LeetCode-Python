'''
    哈希 - 最长连续序列
'''

class Solution:
    def longestConsecutive(self, nums):  # 使用哈希集合
        num_set = set(nums)  # 自动去重
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                cur_num = num
                cur_length = 1

                while cur_num + 1 in num_set:
                    cur_length += 1
                    cur_num += 1
                
                longest = max(longest, cur_length)

        return longest
    
# test
nums = [100, 4, 200, 1, 3, 2]
print(Solution.longestConsecutive(Solution, nums))