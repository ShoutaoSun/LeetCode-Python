'''
    分割回文串
'''

class Solution:
    def partition(self, s):
        n = len(s)
        ans = []
        path = []

        def dfs(i, start):
            if i == n:
                ans.append(path[:])
                return 

            # 不分割
            if i < n - 1:
                dfs(i+1, start)

            # 分割
            t = s[start: i+1]
            if t == t[::-1]:
                path.append(t)
                dfs(i+1, i+1)
                path.pop()  # 恢复现场
        dfs(0, 0)
        return ans

# test
s = "aab"
print(Solution.partition(Solution, s))
