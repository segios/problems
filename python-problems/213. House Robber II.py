# https://leetcode.com/problems/house-robber-ii/
# 213. House Robber II
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

        def findMaxRob(start, end):
            robs = [nums[start], 0] if start % 2 == 0 else  [0, nums[start]]
            for h in range(start+1, end):
                robIndex = h % 2
                prevRobIndex = (h-1) % 2
                robs[robIndex] = max(robs[prevRobIndex], nums[h] + robs[robIndex])

            return max(robs[0], robs[1])
        rob1 = findMaxRob(0, len(nums)-1)
        rob2 = findMaxRob(1, len(nums))
        return max(rob1, rob2)

class SolutionDemo:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(self.rob_simple(nums[:-1]), self.rob_simple(nums[1:]))

    def rob_simple(self, nums: List[int]) -> int:
        t1 = 0
        t2 = 0
        for current in nums:
            temp = t1
            t1 = max(current + t2, t1)
            t2 = temp

        return t1

solution = Solution()

res = solution.rob([2,3,2])
print(res)  

res = solution.rob([2,1,1,2])
print(res)   

res = solution.rob([1,2,3,1])
print(res)   

res = solution.rob([2,7,9,3,1])
print(res)   