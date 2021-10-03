# https://leetcode.com/problems/subsets/
# 78. Subsets
# Medium
# Array, Backtracking, Bit Manipulation
# A
# 

from typing import List
from collections import Counter
import itertools

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
                return
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output

class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            l = len(res)
            for s in range(l):
                copy = res[s][:]
                copy.append(n)
                res.append(copy)

        return res
        

solution = Solution()

res = solution.subsets([1,2,3])
print(res)    

n = 3
nth_bit = 1 << n
for i in range(2**n):
    # generate bitmask, from 0..00 to 1..11
    bitmask = bin(i | nth_bit)[3:]
  

for i in range(2**n, 2**(n + 1)):
    # generate bitmask, from 0..00 to 1..11
    bitmask = bin(i)[3:]
    print (bitmask)