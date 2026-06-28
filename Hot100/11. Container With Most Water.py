'''
    双指针 - 盛最多水的容器
'''

class Solution:
    def maxArea(self, height):
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            length = right - left
            h = min(height[left], height[right])
            area = length * h
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
    
# test
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution.maxArea(Solution, height))