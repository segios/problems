# https://leetcode.com/problems/search-insert-position/
# 35. Search Insert Position
# Easy
# Binary Search, Array
# A


from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, h= 0, len(nums)-1

        while l <= h:
            m= l + (h-l)//2
            if nums[m] == target:
                return m
            if nums[m] > target:
                h= m-1
            else :
                l = m + 1
        return l



solution = Solution()


res = solution.searchInsert([1,3,5,6], 2)
print (res)

res = solution.searchInsert([1,3,5,6], 5)
print (res)