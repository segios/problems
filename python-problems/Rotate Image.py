# https://leetcode.com/problems/rotate-image/
# 48. Rotate Image
# Medium
# Arrays
# A/B
# 

from typing import List
from collections import Counter

class SolutionTransoonseReflect:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)
    
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]



class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix :
            return;

        xs, ys = 0, 0
        xl, yl = len(matrix[0]), len(matrix)
        for y in range(int(yl / 2)):
            for x in range(xs, xl-1):
                curx, cury = x, y
                v1 = matrix[cury][curx]
                v2 = matrix[curx][xl-1]
                
                matrix[curx][xl-1] = v1

                v3 = matrix[yl-1][xl-1-x + xs]
                matrix[yl-1][xl-1-x + xs] = v2

                v4 = matrix[xl-1 - x + xs][cury]
                matrix[xl-1 - x + xs][cury] = v3

                matrix[cury][curx] = v4

            xl -= 1
            yl -= 1
            xs += 1


solution = Solution()

m = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
#m = [[1,2],[3,4]]
solution.rotate(m)
print(m)    