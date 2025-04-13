'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example:
Input: root = [1,null,2,3]
Output: [3,2,1]
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []

        def dfs(node):
            if node is None:
                return 
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)
        dfs(root)
        return result