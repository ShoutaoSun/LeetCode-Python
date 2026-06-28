'''
    双指针 - 接雨水
'''

class Solution:
    def trap1(self, height):  # 动态规划
        sum = 0
        height_left = [0] * len(height)
        height_right = [0] * len(height)

        # 从左到右遍历
        left = 0
        for i in range(len(height)):
            height_left[i] = max(left - height[i], 0)
            left = max(height[i], left)
        # print(height_left)

        # 从右到左遍历
        right = 0
        for j in range(len(height)-1, -1, -1):
            height_right[j] = max(right - height[j], 0)
            right = max(height[j], right)
        # print(height_right)
        
        for k in range(len(height)):
            sum += min(height_left[k], height_right[k])
        return sum
    
    def trap2(self, height):  # 双指针
        sum = 0
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])

            if height[left] < height[right]:
                sum += leftMax - height[left]
                left += 1
            else:
                sum += rightMax - height[right]
                right -= 1

        return sum

# test
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution.trap1(Solution, height))
print(Solution.trap2(Solution, height))