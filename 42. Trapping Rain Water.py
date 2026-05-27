'''
    单调栈 - 接雨水
    思路：按行方向计算雨水面积
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = [0]
        sum = 0

        for i in range(1, len(height)):
            while stack and height[i] > height[stack[-1]]:
                mid = height[stack.pop()]
                if stack:
                    h = min(height[stack[-1]], height[i]) - mid
                    w = i - stack[-1] - 1
                    sum += h * w
            stack.append(i)
        return sum

# test
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution.trap(Solution(), height))