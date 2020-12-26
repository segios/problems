# https://leetcode.com/problems/missing-number/
# 268. Missing Number
# Easy
# Arrays, Bit Manipulation
# B
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        summ = int((n+1) * n / 2)
        # total_sum = n * (n + 1 ) // 2
        for num in nums:
            summ -= num
        return summ

solution = Solution()

res = solution.missingNumber([3,0,1])
print(res)


class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return int(n*(n+1)/2 - sum(nums))

class Solution2:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing