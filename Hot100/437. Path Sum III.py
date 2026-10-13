'''
    路径总和 III
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum):
        from collections import defaultdict

        # 哈希表的初始化
        cnt = defaultdict(int)
        cnt[0] = 1  # 空前缀的和为 0，出现了一次
        ans = 0

        def dfs(node, s):
            if node is None:
                return 
            nonlocal ans
            s += node.val
            ans += cnt[s - targetSum]
            cnt[s] += 1
            dfs(node.left, s)
            dfs(node.right, s)
            cnt[s] -= 1  # 恢复现场

        dfs(root, 0)
        return ans
