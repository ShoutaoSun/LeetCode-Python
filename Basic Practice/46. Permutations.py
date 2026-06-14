'''
    回溯算法练习 - 全排列
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.backtracking(nums, [], [False] * len(nums), result)
        return result
        
    def backtracking(self, nums, path, used, result):
        # 确定终止条件
        if len(path) == len(nums):
            result.append(path[:])
            return 
        
        # 单层迭代
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            self.backtracking(nums, path, used, result)
            path.pop()
            used[i] = False

# test
nums = [1, 2, 3]
print(Solution.permute(Solution(), nums))