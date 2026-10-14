'''
    课程表
'''

class Solution:
    def canFinish(self, numCourses, prerequisites):
        # 构建有向图 g
        g = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            g[b].append(a)

        colors = [0] * numCourses
        # 返回 True 代表找到了环
        def dfs(x):
            colors[x] = 1
            for y in g[x]:
                if colors[y] == 1 or colors[y] == 0 and dfs(y):
                    return True
            colors[x] = 2
            return False

        for i, c in enumerate(colors):
            if c == 0 and dfs(i):
                return False
        return True
        