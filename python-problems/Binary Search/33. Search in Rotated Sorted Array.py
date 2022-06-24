# https://leetcode.com/problems/search-in-rotated-sorted-array/
# 33. Search in Rotated Sorted Array
# Medium
# Binary Search, Array
# 


from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        m = (l+r)//2
        if len(nums) == 1:
            if nums[0] != target:
                return -1
            return 0

        while m+1 < len(nums) and l <=r  and nums[m] > nums[m+1]:
            if nums[m] > nums[r]:
                l = m+1
            elif nums[m] < nums[l]:
                r = m-1
            m = (l+r) // 2
     #   m = l
        def binSearch(l, r):
            
            while l <= r:
                m1 = (l+r)//2
                if nums[m1] == target:
                    return m1
                if nums[m1] < target:
                    l = m1 + 1
                else:
                    r = m1 - 1
            return -1

        res1 = binSearch(0, m-1)
        if res1 >= 0:
            return res1
        res1 = binSearch(m, len(nums)-1)
        return res1




solution = Solution()

res = solution.search([4,5,6,7,0,1,2], 0)
print (res)

