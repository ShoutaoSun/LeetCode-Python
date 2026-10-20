'''
    组合总和
'''

class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        path = []

        def dfs(i, left):
            if left == 0:
                ans.append(path[:])
                return

            if i == len(candidates) or left < 0:
                return

            dfs(i+1, left)  # 不选

            # 选
            path.append(candidates[i])
            dfs(i, left-candidates[i])
            path.pop()

        dfs(0, target)
        return ans

# test
candidates = [2, 3, 6, 7]
target = 7
print(Solution.combinationSum(Solution, candidates, target))
