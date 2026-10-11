'''
    将有序数组转换为二叉搜索树
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        m = len(nums) // 2
        left = self.sortedArrayToBST(nums[:m])
        right = self.sortedArrayToBST(nums[m + 1:])
        return TreeNode(nums[m], left, right)
    