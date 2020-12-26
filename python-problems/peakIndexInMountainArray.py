# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# 852. Peak Index in a Mountain Array
# Easy
# Binary Search
# A
# 


from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, h = 1, len(arr)-1
        while l <= h:
            i = l + (h-l) // 2
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                return i
            elif arr[i] > arr[i+1] and arr[i] < arr[i-1]:
                h = i-1
            else:
                l = i+1
        return -1

class Solution1:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range( 1, len(arr)-1):
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                return i
        return -1

class Solution3(object):
    def peakIndexInMountainArray(self, A):
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mi = (lo + hi) / 2
            if A[mi] < A[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return lo

solution = Solution()

res = solution.peakIndexInMountainArray([0,10,5,2])
print(res) 
