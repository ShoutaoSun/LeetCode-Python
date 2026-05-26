'''
    单调栈专题练习
'''

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = [-1] * len(nums1)

        # 暴力解法 - 可通过，但时间复杂度太高
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j]:
        #             for k in range(j+1, len(nums2)):
        #                 if nums2[k] > nums2[j]:
        #                     result[i] = nums2[k]
        #                     break

        # 单调栈
        stack = [0]
        for i in range(1, len(nums2)):
            if nums2[i] <= nums2[stack[-1]]:
                stack.append(i)
            else:
                while stack and nums2[i] > nums2[stack[-1]]:
                    if nums2[stack[-1]] in nums1:
                        result[nums1.index(nums2[stack[-1]])] = nums2[i]
                    stack.pop()
                stack.append(i)

        return result
        
# test
nums1 = [4, 1, 2, 0]
nums2 = [3, 4, 2, 0, 1]
print(Solution.nextGreaterElement(Solution(), nums1, nums2))