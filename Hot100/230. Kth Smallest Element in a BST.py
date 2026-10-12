'''
    二叉搜索树中第 k 小的元素
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        def dfs(node):
            if not node:
                return -1  # -1 表示没找到
            left_res = dfs(node.left)
            if left_res != -1:
                return left_res
            nonlocal k
            k -= 1
            if k == 0:
                return node.val
            return dfs(node.right)
        return dfs(root)
