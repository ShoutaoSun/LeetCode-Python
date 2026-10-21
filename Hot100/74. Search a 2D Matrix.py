'''
    搜索二维矩阵
'''

class Solution:
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        up, down = 0, m - 1
        while up <= down:
            mid1 = (up + down) // 2
            if matrix[mid1][0] <= target:
                up = mid1 + 1
            else:
                down = mid1 - 1
        row = up - 1

        if row < 0:
            return False

        left, right = 0, n - 1
        while left <= right:
            mid2 = (left + right) // 2
            if matrix[row][mid2] == target:
                return True
            elif matrix[row][mid2] < target:
                left = mid2 + 1
            else:
                right = mid2 - 1
        return False

# test
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 1
print(Solution.searchMatrix(Solution, matrix, target))
