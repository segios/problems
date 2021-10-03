# https://leetcode.com/problems/subarray-sum-equals-k/
# 560. Subarray Sum Equals K
# Medium
# Arrays
# B

from collections import defaultdict
import sys
from typing import DefaultDict, List, Tuple

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0

        if(nums is None or len(nums) == 0):
            return res
        
        dic = defaultdict(int)
        dic[0] = 1


        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in dic:
                res += dic[sum - k]
            dic[sum] += 1
        return res                

class SolutionSum1:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0

        if(nums is None or len(nums) == 0):
            return res
        
        for i in range(len(nums)):
            sum = 0
            for l in range(i, len(nums)):
                sum += nums[l]
                if sum == k:
                    res += 1
        return res                


class SolutionSum:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0

        if(nums is None or len(nums) == 0):
            return res
        
        prefixSumArr = [0] * len(nums)
        prefixSumArr[0] = nums[0]

        for i in range(1, len(nums)):
            prefixSumArr[i] = nums[i] + prefixSumArr[i-1]

        for i in range(len(nums)):
            for l in range(i, len(prefixSumArr)):
                if prefixSumArr[l] == k:
                    res += 1
                prefixSumArr[l] -= nums[i]
        return res                

solution = Solution()

res = solution.subarraySum([-1,-1,1], 0)
print (res)


res = solution.subarraySum([1], 0)
print (res)

res = solution.subarraySum([1,1,1], 2)
print (res)


res = solution.subarraySum([1,2,3], 3)
print (res)









