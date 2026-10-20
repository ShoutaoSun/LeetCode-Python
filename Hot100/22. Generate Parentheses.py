'''
    括号生成
'''

class Solution:
    def generateParenthesis(self, n):
        ans = []
        path = [''] * (n * 2)

        def dfs(left, right):
            if right == n:  # 填完 2n 个括号
                ans.append(''.join(path))
                return
            if left < n:  # 可填左括号
                path[left + right] = '('
                dfs(left + 1, right)
            if right < left:  # 可填右括号
                path[left + right] = ')'
                dfs(left, right + 1)
        
        dfs(0, 0)
        return ans

# test
n = 3
print(Solution.generateParenthesis(Solution, n))
