'''
    所有可能的路径 - ACM 版本
'''

import ast

graph = ast.literal_eval(input())

n = len(graph)  # 图中节点的数量

ans = []
path = [0]

def dfs(cur):
    if cur == n - 1:
        ans.append(path[:])
        return 
    
    for next in graph[cur]:
        path.append(next)
        dfs(next)
        path.pop()

dfs(0)
print(ans)