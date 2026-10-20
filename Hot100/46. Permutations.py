'''
    全排列
'''

class Solution(object):
    def permute(self, nums):
        n = len(nums)
        path = [0] * n
        on_path = [False] * n
        ans = []

        def dfs(i):
            if i == n:
                ans.append(path[:])  # python2
                return
            for j, on in enumerate(on_path):
                if not on:
                    path[i] = nums[j]
                    on_path[j] = True
                    dfs(i + 1)
                    on_path[j] = False
        dfs(0)
        return ans
