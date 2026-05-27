'''
    单调栈 - 柱状图中最大的矩形
    寻找两侧较小的元素
'''

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.insert(0, 0)  # 在最前面插入一个 0
        heights.append(0)  # 在最后面插入一个 0
        stack = [0]
        result = 0

        for i in range(1, len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                mid = heights[stack.pop()]
                if stack:
                    area = (i - stack[-1] - 1) * mid
                    result = max(result, area)
            stack.append(i)
        
        return result
    
# test
heights = [2, 1, 5, 6, 2, 3]
print(Solution.largestRectangleArea(Solution(), heights))