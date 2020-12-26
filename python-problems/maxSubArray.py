# https://leetcode.com/problems/maximum-subarray/
# 53. Maximum Subarray
# Easy
# Dynamic Programming, Divide and Conquer, Array
# D
# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
# https://leetcode.com/problems/sliding-window-maximum/
# https://leetcode.com/problems/gas-station/
# https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/
# https://leetcode.com/problems/super-washing-machines/solution/
# https://leetcode.com/problems/super-washing-machines/discuss/654317/Explanation-(proof)-of-why-the-solution-works
 
import sys
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        maxsum = nums[0]
        sum = nums[0]
        for  i in range( 1, len(nums)):
            
            if(nums[i] + sum > maxsum):
                maxsum = max(maxsum, nums[i] + sum)
                sum += nums[i]
            else:
                sum += nums[i]

        return max(maxsum, sum)

        
solution = Solution()

res = solution.maxSubArray([2,7,9,3,1])
print (res)

res = solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print (res)


res = solution.maxSubArray([-1,-2])
print (res)


class SolutionGreedy:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        curr_sum = max_sum = nums[0]

        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
            
        return max_sum


class SolutionDP:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        max_sum = nums[0]
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1] 
            max_sum = max(nums[i], max_sum)

        return max_sum