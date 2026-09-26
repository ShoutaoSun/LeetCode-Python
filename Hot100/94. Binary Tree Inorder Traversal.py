'''
    中序遍历
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal1(self, root):  # 递归法
        res = []
        def dfs(root):
            if not root:
                return 

            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res

    def inorderTraversal2(self, root):  # Morris 遍历
        res = []

        while root:
            if root.left:
                pre = root.left  # pre 是中序遍历中 root 的上一个节点
                while pre.right and pre.right is not root:
                    pre = pre.right

                # root 的左子树尚未访问
                if pre.right is None:
                    pre.right = root
                    root = root.left
                    continue

                # root 的左子树访问完毕，恢复原样
                pre.right = None

            res.append(root.val)
            root = root.right
        return res