# https://leetcode.com/problems/sum-of-all-subset-xor-totals/
# 1863. Sum of All Subset XOR Totals
# Easy
# Arrays, Backtracking
# 

from typing import List
import copy
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []
        res = 0

        def calcSubsetsSums(start:int):
            tmpSum = 0
            for i in range(start, len(subsets)):
                ss = subsets[i]
                tmp = 0
                for num in ss:
                    tmp ^= num
                tmpSum += tmp
            return tmpSum

        start = 0
        for n in nums: 
            nesSubsets = copy.deepcopy(subsets)

            nesSubsets.append([n])
            for ss in subsets:
                ss.append(n)
                nesSubsets.append(ss)
            subsets = nesSubsets
            res += calcSubsetsSums(start)
            start = len(subsets)
        return res

solution = Solution()

res = solution.subsetXORSum([5,1,6])
print (res)




