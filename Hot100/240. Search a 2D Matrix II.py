'''
    矩阵 - 搜索二维矩阵 II
'''

class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])

        i = 0
        j = n - 1

        while i < m and j >= 0:
            if matrix[i][j] > target:
                j -= 1    
            elif matrix[i][j] < target:
                i += 1
            else:
                return True
        
        return False
    
# test
matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
] 
target = 5
print(Solution.searchMatrix(Solution, matrix, target))