# https://leetcode.com/problems/find-the-duplicate-number/
# 287. Find the Duplicate Number
# Medium
# Arrays, Binary Search, Two Pointers
# 

from typing import List
from collections import deque

# There is an O(n*log(n)) solution which matches the stated constraints and
#  which might be easier to come up with for people who haven't seen the
#  tortoise and hare trick. Do a binary search on the set of numbers [1,...,n]. 
# For each number, count how many elements of the array are <= or >= that number. 
# Recurse as appropriate.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:




solution = Solution()

res = solution.findDuplicate([2,2,2,2,2])
print(res)    

 
#  class Solution {
# public:
#     int findDuplicate(vector<int>& nums) {
#         int l=1, r=nums.size()-1;
#         while (true) {
#             int mid = (l+r)/2;
#             int leq = 0;
#             int geq = 0;
#             for (int n: nums) {
#                 if (n <= mid)
#                     ++leq;
#                 if (n >= mid)
#                     ++geq;
#             }
#             if (leq > mid) r = mid;
#             if (geq > nums.size() - mid) l = mid;
#             if (l==r) return l;
#             if (l==mid) ++l;
#             else --r;
#         }
#     }
# };