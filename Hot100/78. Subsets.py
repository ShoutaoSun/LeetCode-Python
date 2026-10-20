'''
    子集
'''

class Solution:
    def subsets(self, nums):
        n = len(nums)
        ans = []
        path = []

        def dfs(i):
            if i == n:
                ans.append(path.copy())  # path 会变化，所以应当固定下来 Python3
                # ans.append(path[:])  # Python
                return
            dfs(i+1)  # 如果不选的话直接递归下一个
            
            path.append(nums[i])  # 选此元素
            dfs(i+1)
            # 由于是在路径后面添加元素，所以递归之前是什么样，递归之后也应该是什么样
            # 所以在返回之前，应当将其恢复至递归之前的样子
            path.pop()

        dfs(0)
        return ans
