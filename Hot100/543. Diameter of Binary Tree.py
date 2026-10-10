'''
    二叉树的直径
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        ans = 0

        def dfs(node):
            if node is None:
                return 0
            l_len = dfs(node.left)
            r_len = dfs(node.right)
            nonlocal ans  # Python3 的用法
            ans = max(ans, l_len + r_len)  # 两条链拼成路径
            
            return max(l_len, r_len) + 1

        dfs(root)
        return ans
    