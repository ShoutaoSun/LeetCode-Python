'''
    跳跃游戏 II
'''

class Solution:
    def jump(self, nums):
        ans = 0
        cur_end = 0  # 已建造的桥的右端点
        next_end = 0  # 下一座桥的右端点的最大值

        for i in range(len(nums) - 1):
            next_end = max(next_end, i + nums[i])
            if i == cur_end:  # 无路可走，必须建桥
                cur_end = next_end
                ans += 1
        return ans
        