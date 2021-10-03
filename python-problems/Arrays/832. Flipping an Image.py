# https://leetcode.com/problems/flipping-an-image/
# 832. Flipping an Image
# Easy
# Arrays
# A

from typing import List

class Solution1:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = [(1-w for w in reversed(r)) for r in image]
        return ans

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        
        rowLen = len(image[0])
        
        halfLen = rowLen // 2
        
        for col in range (len(image)):
            for row in range (halfLen):
                
                x = image[col][row]
                lx = image[col][rowLen - row - 1]
                if x == 1:
                    image[col][rowLen - row - 1] = 0
                else:
                    image[col][rowLen - row - 1] = 1
                    
                if lx == 1:
                    image[col][row] = 0
                else:
                    image[col][row] = 1

        
            if (rowLen % 2 == 1):
                s = image[col][halfLen]
                if s == 1:
                    image[col][halfLen] = 0
                else:
                    image[col][halfLen] = 1

        return image


solution = Solution()
res = solution.flipAndInvertImage([[1,0,1]])
print (res)

res = solution.flipAndInvertImage([[1,0,0,1]])
print (res)




