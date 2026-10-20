'''
    N 皇后
'''

class Solution:
    def solveNQueens(self, n):
        ans = []
        queens = [0] * n
        col = [False] * n
        diag1 = [False] * (n * 2 - 1)
        diag2 = [False] * (n * 2 - 1)
        def dfs(r):
            if r == n:  # 放满 n 行，证明找到了一个解
                ans.append(['.' * c + 'Q' + '.' * (n - 1 - c) for c in queens])
                return 
            for c, ok in enumerate(col):  # 枚举第 r 行的每一列
                if not ok and not diag1[r + c] and not diag2[r - c]:
                    queens[r] = c
                    col[c] = diag1[r + c] = diag2[r - c] = True  # 皇后，标记占用
                    dfs(r + 1)
                    col[c] = diag1[r + c] = diag2[r - c] = False  # 恢复现场（回溯）
        dfs(0)
        return ans

# test
n = 4
print(Solution.solveNQueens(Solution, n))
