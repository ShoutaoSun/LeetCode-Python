'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
'''

from collections import deque

class MyQueue(object):
    def __init__(self):
        self.queue = deque()
    
    def pop(self, val):
        if self.queue and val == self.queue[0]:
            self.queue.popleft()
        
    def push(self, val):
        while self.queue and val > self.queue[-1]:
            self.queue.pop()
        self.queue.append(val)

    def front(self):
        return self.queue[0]

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        queue = MyQueue()
        result = []
        for i in range(k):
            queue.push(nums[i])
        result.append(queue.front())
        for i in range(k, len(nums)):
            queue.pop(nums[i - k])
            queue.push(nums[i])
            result.append(queue.front())
        return result

# test
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Solution.maxSlidingWindow(Solution(), nums, k))