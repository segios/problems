# https://leetcode.com/problems/permutations/
# 46. Permutations
# Medium
# Backtracking
# A
# 

import copy 
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        if(len(nums) == 0):
            return res

        res.append([ nums[0] ])
        
        for i in range(1, len(nums)):
            currentLength = len(res)
            resTmp = []
            for c in range(i+1):
                resTmp = resTmp + copy.deepcopy(res) 
            res = resTmp
            pos = 0
            c = 0
            for x in range(len(res)):        
                res[x].insert(pos, nums[i])
                c += 1
                if c >= currentLength:
                    c = 0
                    pos += 1
        return res


class SolutionBacktrack:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0):
            # if all integers are used up
            if first == n:  
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first 
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        output = []
        backtrack()
        return output

solution = Solution()

res = solution.permute([1,2,3])
print(res)    
