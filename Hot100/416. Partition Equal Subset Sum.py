'''
    分割等和子集
'''

class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        # dp[j] 表示能否凑出和为 j 的子集
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):  # 倒序遍历
                dp[j] = dp[j] or dp[j - num]  # 当前数字可选可不选
                if dp[target]:
                    return True
        return dp[target]
