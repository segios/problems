# https://leetcode.com/problems/sqrtx/
# 69. Sqrt(x)
# Easy
# Math, Binary Search
# 

from typing import List
from collections import deque
from _treeHelpers import *

class Solution:
    def mySqrt(self, num: int) -> int:
        if num == 0:
            return 0
        if num == 1:
            return 1

        high = num >> 1
        low = 2		
        middle = low  + (high  - low ) // 2
        while low <= high:
            middle = low  + (high  - low ) // 2 
            res = middle * middle
            if res == num:
                return middle 		
            elif res > num:			
                high = middle-1			
            else:
                low = middle+1		

        # if(middle * middle > num):
        #     middle -= 1

        return high

solution = Solution()

res = solution.mySqrt(100)
print(res)

res = solution.mySqrt(8)
print(res)

res = solution.mySqrt(22)
print(res)

res = solution.mySqrt(5)
print(res)