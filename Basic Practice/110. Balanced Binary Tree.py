'''
Given a binary tree, determine if it is height-balanced.

Example:
Input: root = [3,9,20,null,null,15,7]
Output: true
'''

class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.get_height(root) != -1

    def get_height(self, node):
        if not node:
            return 0
        left = self.get_height(node.left)
        right = self.get_height(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1