# https://leetcode.com/problems/combination-sum/
# 39. Combination Sum
# Medium
# Arrays, Backtracking
# A
# 

from typing import List
from collections import Counter


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def searchTarget (nums: List[int], startIndex, newTarget: int, res : List[int] ):
            
            for i in range(startIndex, len(nums)):
                if (nums[i] <= newTarget):
                    res.append(nums[i])
                    nextTarget = newTarget - nums[i]
                    if nextTarget == 0:
                        result.append(res[:])
                    elif (nextTarget > 0):
                        searchTarget (nums, i, nextTarget, res)
                    res.pop()
            
        searchTarget (candidates, 0, target, [])
        return result


solution = Solution()
res = solution.combinationSum([2,3,6,7], 7)
print(res)    