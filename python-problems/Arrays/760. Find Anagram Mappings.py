# https://leetcode.com/problems/find-anagram-mappings/
# 760. Find Anagram Mappings
# Easy
# Arrays, Hash Table
# A
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subElDic = {}

        for i in range(len(nums)):
            sub = target - nums[i]
            if nums[i] in subElDic :
                return [i, subElDic[nums[i]]]
            subElDic[sub] = i


solution = Solution()

res = solution.twoSum([2,7,11,15], 9)
print (res)




