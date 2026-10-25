'''
    数据流的中位数
'''

import heapq

class MedianFinder:
    def __init__(self):
        self.left = []  # 最大堆
        self.right = []  # 最小堆

    def addNum(self, num):
        if len(self.left) == len(self.right):
            heapq.heappush_max(self.left, heapq.heappushpop(self.right, num))
        else:
            heapq.heappush(self.right, heapq.heappushpop_max(self.left, num))
        
    def findMedian(self):
        if len(self.left) > len(self.right):
            return self.left[0]
        return (self.left[0] + self.right[0]) / 2
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
