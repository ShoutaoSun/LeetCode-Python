'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
'''

import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map_ = {}
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1
        
        pri_que = []
        for key, fre in map_.items():
            heapq.heappush(pri_que, (fre, key))
            if len(pri_que) > k:
                heapq.heappop(pri_que)
            
        result = [0] * k
        for i in range(k - 1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result

# test
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(Solution.topKFrequent(Solution(), nums, k))