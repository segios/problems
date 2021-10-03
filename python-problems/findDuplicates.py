# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# 442. Find All Duplicates in an Array
# Medium
# Arrays
# A/B
# Could you do it without extra space and in O(n) runtime?

from typing import List
from collections import Counter


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = set()
        for i in range(len(nums)):
            x = nums[i]
            while x != i+1:
                y = nums[x-1]
                if y == x:
                    res.add(x)
                    nums[i] = x
                    break
                nums[x-1] = x
                x = y
            nums[i] = x

        return list(res)


class Solution1:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        map = Counter(nums)
        for s in map:
            if map[s] > 1:
                res.append(s)
        return res


solution = Solution()

res = solution.findDuplicates([4,3,2,7,8,2,3,1])
print(res)    