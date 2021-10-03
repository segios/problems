# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# 448. Find All Numbers Disappeared in an Array
# Easy
# Arrays
# B
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        r = []
        s= set(nums)
        for n in range(len(nums)+1):
            if not(n in s) and n != 0 :
                r.append(n)
        return r

    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        for idx in range(len(nums)):                       
            while nums[nums[idx]-1] != nums[idx]: # value at target index misplaced
                nums[nums[idx]-1], nums[idx] = nums[idx], nums[nums[idx]-1]  # swap

        return [idx+1 for idx, num in enumerate(nums) if num != idx + 1] 

        
solution = Solution()

res = solution.findDisappearedNumbers([1,1])
print(res)

class Solution1(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # Iterate over each of the elements in the original array
        for i in range(len(nums)):
            
            # Treat the value as the new index
            new_index = abs(nums[i]) - 1
            
            # Check the magnitude of value at this new index
            # If the magnitude is positive, make it negative 
            # thus indicating that the number nums[i] has 
            # appeared or has been visited.
            if nums[new_index] > 0:
                nums[new_index] *= -1
        
        # Response array that would contain the missing numbers
        result = []    
        
        # Iterate over the numbers from 1 to N and add all those
        # that have positive magnitude in the array 
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                result.append(i)
                
        return result        