'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example:
Input: root = [1,2,2,3,4,4,3]
Output: true
'''

from collections import deque

class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        
        queue = deque([root.left, root.right])
        while queue:
            level_vals = []
            if len(level_vals) % 2 != 0:
                return False
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur:
                    level_vals.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    level_vals.append(None)
            if level_vals != level_vals[::-1]:
                return False
        return True