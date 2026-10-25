'''
    跳跃游戏
'''

class Solution:
    def canJump(self, nums):
        mx = 0
        for i, jump in enumerate(nums):
            if i > mx:
                return False
            mx = max(mx, i + jump)
            if mx >= len(nums) - 1:  # 提前截断
                return True
        