# https://leetcode.com/problems/trapping-rain-water/
# 42. Trapping Rain Water
# Hard
# Arrays, Stack, Two pointers, Dynamic Programming, Monotonic Stack
# C

import sys
from typing import List, Tuple
from collections import deque

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        lmax, rmax = 0, 0
        res = 0
        while left < right:
            if height[left] <  height[right]:
                if height[left] > lmax:
                    lmax = height[left]
                else:
                    res += lmax - height[left]
                left += 1
            else:
                if height[right] > rmax:
                    rmax = height[right]
                else:
                    res += rmax - height[right] 
                right -= 1
        return res



class SolutionStk:
    def trap(self, height: List[int]) -> int:
        res = 0
        stk = deque()
        for i in range (len(height)):
            while stk and height[i] > height[stk[-1]]:
                elI = stk.pop()
                if not stk:
                    break
                distance = i - stk[-1] - 1
                bounded_height = min(height[i], height[stk[-1]]) - height[elI]
                res += distance * bounded_height
            stk.append(i)   
        
        return res

class SolutionDP:
    def trap(self, height: List[int]) -> int:
        leftmax, rightmax = [0] * len(height), [0] * len(height)
        leftmax[0] = height[0]
        rightmax[len(height)-1] = height[len(height)-1]

        for i in range (1, len(height)):
            leftmax[i] = max(leftmax[i-1], height[i])

        for i in range (len(height)-2, -1, -1):
            rightmax[i] = max(rightmax[i+1], height[i])            

        res = 0
        for i in range (1, len(height)):
            res += min(leftmax[i], rightmax[i]) - height[i]

        return res

solution = Solution()

res = solution.trap([4,2,2,5])
print (res)

res = solution.trap([0,1,0,2])
print (res)

res = solution.trap([2,1,0,1,3])
print (res)

res = solution.trap([4,2,0,3,2,5])
print (res)

res = solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print (res)





