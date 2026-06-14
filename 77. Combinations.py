'''
    回溯算法练习 - 组合问题
'''

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []  # 存放结果集
        self.backtracking(n, k, 1, [], result)
        return result

    def backtracking(self, n, k, startIndex, path, result):
        # 确定终止条件
        if len(path) == k:
            result.append(path[:])
            return 
        
        # 确定单层递归逻辑
        for i in range(startIndex, n + 1):
            path.append(i)
            self.backtracking(n, k, i + 1, path, result)
            path.pop()

# test
n = 4
k = 2
print(Solution.combine(Solution(), n, k))