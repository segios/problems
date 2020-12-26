# https://leetcode.com/problems/single-number/
# 136. Single Number
# Easy
# Arrays, Bit Manipulation
# A
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r = 0
        for n in nums:
            r  = r ^ n
        return r

solution = Solution()

res = solution.singleNumber([4,1,2,1,2])
print(res)