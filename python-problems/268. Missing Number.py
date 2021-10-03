# https://leetcode.com/problems/missing-number/
# 268. Missing Number
# Easy
# Arrays, Bit Manipulation
# A
from typing import List


class Solution:
    def missingNumber(self, nums):
        nums.sort()

        # Ensure that n is at the last index
        if nums[-1] != len(nums):
            return len(nums)
        # Ensure that 0 is at the first index
        elif nums[0] != 0:
            return 0

        # If we get here, then the missing number is on the range (0, n)
        for i in range(1, len(nums)):
            expected_num = i
            if nums[i] != expected_num:
                return expected_num

class Solution3:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(n+1)

        for i in range(n+1):
            nums[i] += 1
        
        for i in range(n):            
            idx = abs(nums[i])-1
            nums[idx] = -abs(nums[idx])
        
        for i in range(n+1):
            if nums[i] > 0 :
                return i

class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        summ = int((n+1) * n / 2)
        summ2 = sum(nums)
        return summ - summ2



solution = Solution()

res = solution.missingNumber([0,1])
print(res)
