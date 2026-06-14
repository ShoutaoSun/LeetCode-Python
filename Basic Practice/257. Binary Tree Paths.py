'''
Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.

Example:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
'''

class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        result = []
        path = []
        if not root:
            return result
        self.traversal(root, path, result)
        return result

    def traversal(self, cur, path, result):
        path.append(cur.val)
        if not cur.left and not cur.right:
            sPath = '->'.join(map(str, path))
            result.append(sPath)
            return
        if cur.left:
            self.traversal(cur.left, path, result)
            path.pop()
        if cur.right:
            self.traversal(cur.right, path, result)
            path.pop()