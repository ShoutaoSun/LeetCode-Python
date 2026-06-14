'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
'''

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [[float('inf')] * n for _ in range(n)]  # Create array
        startx, starty = 0, 0
        count = 1

        for offset in range(1, n // 2 + 1):
            for i in range(starty, n - offset):
                nums[startx][i] = count
                count += 1
            for i in range(startx, n - offset):
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, starty, -1):
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1):
                nums[i][starty] = count
                count += 1
            startx += 1
            starty += 1

        if n % 2 == 1:
            nums[n // 2][n // 2] = count
        return nums
        
# test
n = 3
print(Solution.generateMatrix(Solution(), n))