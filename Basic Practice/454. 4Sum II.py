'''
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

- 0 <= i, j, k, l < n
- nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Example:
Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
'''

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        hashmap = dict()
        for num1 in nums1:
            for num2 in nums2:
                hashmap[num1 + num2] = hashmap.get(num1 + num2, 0) + 1
        
        cnt = 0
        for num3 in nums3:
            for num4 in nums4:
                tmp = - num3 - num4
                if tmp in hashmap:
                    cnt += hashmap[tmp]
        return cnt
    
# test
nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]
print(Solution.fourSumCount(Solution(), nums1, nums2, nums3, nums4))