# https://leetcode.com/problems/jump-game/
# 55. Jump Game
# Medium
# Dynamic Programming
# A
# 

from typing import List
from collections import Counter


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True

        zeroIndex = -1
        for i in reversed(range(len(nums)-1)):
            if zeroIndex > 0:
                if nums[i] + i > zeroIndex:
                    zeroIndex = -1
            if nums[i] == 0 and zeroIndex < 0:
                zeroIndex = i
        return not (zeroIndex >= 0)
                



solution = Solution()

res = solution.canJump([2,0,1,0,1])
print(res)  

res = solution.canJump([2,3,1,1,4])
print(res)  

res = solution.canJump([3,2,1,0,4])
print(res)  
