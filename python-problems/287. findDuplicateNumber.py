# https://leetcode.com/problems/find-the-duplicate-number/
# 287. Find the Duplicate Number
# Medium
# Arrays, Binary Search, Two Pointers
# C

from typing import List
from collections import deque


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tmp = [0] * len(nums)
        for i in range(len(nums)):
            if(tmp[nums[i] - 1] != 0):
                return nums[i]
            tmp[nums[i] - 1] = nums[i]


class Solution1:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1): # use binary search ?
            if(nums[i] == nums[i+1]):
                return nums[i]


solution = Solution()

res = solution.findDuplicate([1,3,4,2,2])
print(res)    