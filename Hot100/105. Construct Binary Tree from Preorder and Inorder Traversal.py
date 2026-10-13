'''
    从前序与中序遍历序列构造二叉树
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        
        left_size = inorder.index(preorder[0])
        left = self.buildTree(preorder[1:1 + left_size], inorder[:left_size])
        right = self.buildTree(preorder[1 + left_size:], inorder[1 + left_size:])
        return TreeNode(preorder[0], left, right)
    