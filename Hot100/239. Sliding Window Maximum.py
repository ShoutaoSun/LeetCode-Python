'''
    子串 - 滑动窗口最大值
'''

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        result = []

        for i in range(len(nums)):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
                
            dq.append(i)
                
            if dq[0] < i - k + 1:
                dq.popleft()

            if i >= k - 1:  # 窗口形成后，记录最大值
                result.append(nums[dq[0]])

        return result


# test
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Solution.maxSlidingWindow(Solution, nums, k))