'''
    寻找两个正序数组的中位数
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        
        left, right = -1, m
        while left + 1 < right:
            i = (left + right) // 2
            j = (m + n - 3) // 2 - i
            if nums1[i] <= nums2[j + 1]:
                left = i
            else:
                right = i

        # 此时 left == right - 1
        i = left
        j = (m + n - 3) // 2 - i
        ai = nums1[i] if i >= 0 else float('-inf')
        bj = nums2[j] if j >= 0 else float('-inf')
        ai1 = nums1[i + 1] if i + 1 < m else float('inf')
        bj1 = nums2[j + 1] if j + 1 < n else float('inf')
        max1 = max(ai, bj)
        min2 = min(ai1, bj1)
        return max1 if (m + n) % 2 else (max1 + min2) / 2

# test
nums1 = [1, 2]
nums2 = [3, 4]
print(Solution.findMedianSortedArrays(Solution, nums1, nums2))
