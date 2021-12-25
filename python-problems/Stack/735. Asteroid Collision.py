# https://leetcode.com/problems/asteroid-collision/
# 735. Asteroid Collision
# Medium
# Array, Stack
# A/B

import sys
from typing import List, Tuple
from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = deque()
        stk.append(asteroids[0])
        for i in range (1, len(asteroids)):
            while stk and  asteroids[i] < 0 < stk[-1]: 
                if stk[-1] < abs(asteroids[i]):
                    stk.pop()
                    continue
                elif stk[-1] == abs(asteroids[i]):
                    stk.pop()
                break    
            else:
                stk.append(asteroids[i])
        
            
        return list(stk)

solution = Solution()

res = solution.asteroidCollision([5,-5])
print (res)


res = solution.asteroidCollision([10,2,-5])
print (res)


res = solution.asteroidCollision([5,10,-5])
print (res)



res = solution.asteroidCollision([-2,-1,1,2])
print (res)

