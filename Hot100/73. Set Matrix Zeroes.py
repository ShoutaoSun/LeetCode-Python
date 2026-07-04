'''
    矩阵 - 矩阵置零
'''

class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        rowZeroflag = any(matrix[0][j] == 0 for j in range(n))
        colZeroflag = any(matrix[i][0] == 0 for i in range(m))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if rowZeroflag:
            for i in range(n):
                matrix[0][i] = 0
        
        if colZeroflag:
            for i in range(m):
                matrix[i][0] = 0

        return matrix

# test
matrix = [[1, 0, 1], [1, 0, 1], [1, 1, 1]]
print(Solution.setZeroes(Solution, matrix))