'''
    二叉树中的最大路径和
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root):
        ans = float("-inf")  # 全局答案，记录所有节点作为拐点时的最大路径和
        def dfs(node):
            if node is None:
                return 0  # 空节点贡献 0
            sum_l = dfs(node.left)  # 左子树最大链和
            sum_r = dfs(node.right)  # 右子树最大链和
            nonlocal ans
            ans = max(ans, sum_l + node.val + sum_r)  # 当前节点 node 是拐点的情况
            return max(max(sum_l, sum_r) + node.val, 0)  # 当前子树最大链和，负数的话舍弃
        
        dfs(root)
        return ans
