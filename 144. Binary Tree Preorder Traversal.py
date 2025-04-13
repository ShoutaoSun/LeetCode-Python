'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example:
Input: root = [1,null,2,3]
Output: [1,2,3]
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        
        def dfs(node):
            if node is None:
                return 
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return result