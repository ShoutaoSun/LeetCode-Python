'''
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
'''

from collections import deque

class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            sum = 0.0
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                sum += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(sum / size)
        return result            