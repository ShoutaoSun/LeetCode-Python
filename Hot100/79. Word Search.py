'''
    单词搜索
'''

class Solution:
    def exist(self, board, word):
        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            if board[i][j] != word[k]:  # 匹配失败
                return False
            if k == len(word) - 1:  # 匹配成功
                return True
            board[i][j] = ''  # 标记访问过
            for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):
                if 0 <= x < m and 0 <= y < n and dfs(x, y, k + 1):
                    return True
            board[i][j] = word[k]  # 恢复现场
            return False
        return any(dfs(i, j, 0) for i in range(m) for j in range(n)) 

# test
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
word = "ABCCED"
print(Solution.exist(Solution, board, word))
