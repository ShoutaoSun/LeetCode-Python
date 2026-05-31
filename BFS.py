'''
    广度优先搜索 - 算法模板
'''

from collections import deque

grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
rows, cols = 3, 3

q = deque()  # 队列存放待探索的坐标
visited = [[0] * cols for _ in range(rows)]

dir = [
    [0, 1],
    [1, 0],
    [-1, 0],
    [0, -1]
]  # 全局变量，表示 x 和 y 方向的变化

def BFS(grid, visited, x, y):  # x 和 y 为当前节点坐标
    q.append((x, y))
    visited[x][y] = 1  # 遍历过的点要标记访问过了
    
    while q:
        cur = q.popleft()
        for i in range(4):
            next_x = cur[0]
            next_y = cur[1]
            # 判断是否越界
            if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]):
                continue
            # 判断节点是否被遍历过
            if not visited[x][y]:
                q.append((x, y))
                visited[x][y] = 1