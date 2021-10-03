# https://leetcode.com/problems/set-matrix-zeroes/
# 73. Set Matrix Zeroes
# Medium
# Arrays
# B
# 

from typing import List
from collections import Counter

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lastI = len(matrix)-1
        lastJ = len(matrix[0])-1
        zeroCols : List[int] = [-1] * len(matrix[0])
        zeroRows : List[int] = [-1] * len(matrix)

        for i in range (len(matrix)):
            for j in range (len(matrix[i])):
                if matrix[i][j] == 0:
                    zeroCols[j] = 0
                    zeroRows[i] = 0
                #    matrix[i][lastJ] = 0
                 #   matrix[lastI][j] = 0

        for i in range (len(matrix)):
            isZeroRow = zeroRows[i] == 0
#            isZeroRow = matrix[i][lastJ] == 0
            if isZeroRow:
                for j in range (len(matrix[i])):
                    matrix[i][j] = 0
 

        for j in range (len(matrix[0])):
            isZeroCol = zeroCols[j] == 0
            if isZeroCol:
                for i in range (len(matrix)):
                     matrix[i][j] = 0   
        


solution = Solution()

m = [[1,1,1],[1,0,1],[1,1,1]]
solution.setZeroes(m)
print(m)    