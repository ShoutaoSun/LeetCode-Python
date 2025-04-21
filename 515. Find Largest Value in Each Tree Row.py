'''
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Example:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
'''

from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            max_num = float('-inf')
            for _ in range(len(queue)):
                cur = queue.popleft()
                max_num = max(max_num, cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(max_num)
        return result