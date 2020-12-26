# https://leetcode.com/problems/range-sum-query-immutable/
# 303. Range Sum Query - Immutable
# Easy
# Dynamic Programming
# D
 
import sys
from typing import List

class NumArrayCaching1:

    def __init__(self, nums: List[int]):
        self.nums = nums  
        self.cache = {}
        for i in range (len(nums)):
            sum = 0
            for j in range (i,len(nums)):
                sum += nums[j]
                self.cache[(i,j)] = sum

    def sumRange(self, i: int, j: int) -> int:
        return self.cache[(i, j)]

class NumArrayCaching2:

    def __init__(self, nums: List[int]):
        self.nums = nums  
        self.sum = [0] * (len(nums) + 1)

        for i in range (len(nums)):
            self.sum[i + 1] = self.sum[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.sum[j+1] - self.sum[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


solution = NumArrayCaching2([-2, 0, 3, -5, 2, -1])

res = solution.sumRange(1,4)
print(res)