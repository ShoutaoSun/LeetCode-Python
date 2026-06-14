# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # dp 数组中下标为 0 记录不偷该节点所得到的最大金钱，下标为 1 记录偷该节点所得到的最大金钱
        dp = self.traversal(root)
        return max(dp)

    def traversal(self, node):
        if not node:
            return (0, 0)
        
        left = self.traversal(node.left)
        right = self.traversal(node.right)

        val_0 = max(left[0], left[1]) + max(right[0], right[1])  # 不偷当前节点，偷子节点
        val_1 = node.val + left[0] + right[0]  # 偷当前节点，不偷子节点

        return (val_0, val_1)
