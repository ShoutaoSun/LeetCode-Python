'''
    矩阵 - 螺旋矩阵
'''

class Solution:
    def spiralOrder(self, matrix):
        result = []
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = n - 1
        top = 0
        bottom = m - 1

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result

# test
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution.spiralOrder(Solution, matrix))