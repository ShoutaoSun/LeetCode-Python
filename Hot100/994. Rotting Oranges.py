'''
    腐烂的橘子
'''

class Solution(object):
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])  # 行，列
        fresh = 0
        q = []  # 存放腐烂橘子
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    fresh += 1
                elif x == 2:
                    q.append((i, j))  # 一开始就腐烂的橘子

        ans = 0
        while q and fresh:
            ans += 1
            tmp = q
            q = []
            for x, y in tmp:
                for i, j in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        fresh -= 1
                        grid[i][j] = 2
                        q.append((i, j))

        return -1 if fresh else ans  # 别忘记有的橘子不会腐烂
    