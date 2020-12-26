# https://leetcode.com/problems/contains-duplicate/
# 217. Contains Duplicate
# Easy
# Arrays
# A
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for num in nums:
            if num in dic:
                return True
            else:
                dic[num] = 1

        return False

solution = Solution()

res = solution.containsDuplicate([1,2,3])
print (res)

res = solution.containsDuplicate([1,2,3,1])
print (res)


class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
