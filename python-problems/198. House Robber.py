# https://leetcode.com/problems/house-robber/
# 198. House Robber
# Medium
# Dynamic Programming
# A/B
# 

from typing import List
from collections import Counter


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums or  len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        robs = [nums[0], 0]

        for h in range(1, len(nums)):
            robIndex = h % 2
            prevRobIndex = (h-1) % 2
            robs[robIndex] = max(robs[prevRobIndex], nums[h] + robs[robIndex])

        return max(robs[0], robs[1])



solution = Solution()
res = solution.rob([2,1,1,2])
print(res)   

res = solution.rob([1,2,3,1])
print(res)   

res = solution.rob([2,7,9,3,1])
print(res)   