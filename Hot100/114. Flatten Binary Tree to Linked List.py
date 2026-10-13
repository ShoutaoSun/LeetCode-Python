'''
    二叉树展开为链表
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    head = None
    
    def flatten1(self, root):
        if root is None:
            return 
        # 右 -> 左 -> 根
        self.flatten1(root.right)
        self.flatten1(root.left)
        root.left = None
        root.right = self.head  # 在头节点 head 的前面插入
        self.head = root  # 现在头节点是 root

    def flatten2(self, root):
        if root is None:
            return 
        left_tail = self.flatten2(root.left)
        right_tail = self.flatten2(root.right)
        if left_tail:
            left_tail.right = root.right
            root.right = root.left
            root.left = None
        return right_tail or left_tail or root
