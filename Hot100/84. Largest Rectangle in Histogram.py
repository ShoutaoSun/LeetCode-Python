'''
    柱状图中最大的矩形
'''

class Solution(object):
    def largestRectangleArea(self, heights):
        heights.append(-1)
        st = [-1]
        res = 0
        for right, h in enumerate(heights):
            while len(st) > 1 and heights[st[-1]] >= h:
                i = st.pop()
                left = st[-1]
                res = max(res, heights[i] * (right - left - 1))
            st.append(right)
        return res
    