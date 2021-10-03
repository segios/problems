# https://leetcode.com/problems/running-sum-of-1d-array/
# 1480. Running Sum of 1d Array
# Easy
# Arrays
# A

import sys
from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if(not nums or len(nums) == 0):
            return nums

        res = []
        res.append(nums[0])

        for i in range(1, len(nums)):
           res.append(nums[i] + res [i-1])

        return res


solution = Solution()

res = solution.runningSum([1,2,3,4])
print (res)

res = solution.runningSum([1,1,1,1,1])
print (res)

