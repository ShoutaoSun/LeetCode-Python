'''
    二叉树的最大深度
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):  # 自底向上
        if not root:
            return 0
        l_dep = self.maxDepth(root.left)
        r_dep = self.maxDepth(root.right)
        return max(l_dep, r_dep) + 1
        