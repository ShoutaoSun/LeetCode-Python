'''
    岛屿数量
'''

class Solution(object):
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            # 边界条件
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            grid[i][j] = '2'  # 相当于设置一个 flag
            dfs(i, j - 1)  # 左
            dfs(i, j + 1)  # 右
            dfs(i - 1, j)  # 上
            dfs(i + 1, j)  # 下

        ans = 0
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == '1':
                    dfs(i, j)
                    ans += 1
        return ans
    