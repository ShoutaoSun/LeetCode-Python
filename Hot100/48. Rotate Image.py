'''
    矩阵 - 旋转图像
'''

class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()
            
        return matrix
    
# test
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution.rotate(Solution, matrix))