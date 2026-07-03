'''
    子串 - 和为 K 的子数组
'''

class Solution:
    def subarraySum(self, nums, k):
        cnt = {0:1}  # 前缀和为 0 出现过 1 次
        ans = s = 0

        for num in nums:
            s += num
            ans += cnt.get(s - k, 0)
            cnt[s] = cnt.get(s, 0) + 1
            
        return ans
    
# test
nums = [1, 1, 1]
k = 2
print(Solution.subarraySum(Solution, nums, k))
