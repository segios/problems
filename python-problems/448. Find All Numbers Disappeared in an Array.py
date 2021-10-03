# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# 448. Find All Numbers Disappeared in an Array
# Easy
# Arrays
# 
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        
        res = [] 
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(i+1)
        return res                 
        return [i+1 for i, num in enumerate(nums) if num != i+1] 

solution = Solution()

res = solution.findDisappearedNumbers([4,3,2,7,8,2,3,1])
print(res)            


class Solution1:
    def findDisappearedNumbersNoExtra(self, nums: List[int]) -> List[int]:
        result = []
        if not nums:
            return []
        for i in range(1, len(nums)+1):
            if not i in nums:
                result .append(i)  
        
        return result
    
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        if not nums:
            return []
        return list({i for i in range(1,len(nums)+1)} - set(nums) )

class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        return list(set(range(1, len(nums)+1))-set(nums))        

class Solution3:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        goal = set(range(1,len(nums)+1))
        return list(goal - set(nums))        


class Solution4:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        assumptions: given constraints
        test cases: given test cases
        solutions: 
        1) Make a set out of the range of numbers and set of nums and use .difference()
        O(4n complexity), O(2n) space
        2) Sort the list. Traverse the list and if two neighboring digits have a difference of more than 1, add the range of values to another list. Add the range between the 1 and the 1st element to the list. Add the range between the last element and the length of the list to the other list. O(nlogn + n + n) time and O(n) space
        """
        return (set(range(1, len(nums)+1)))-set(nums)
        
        # nums.sort()
        # disappeared = []
        # disappeared += range(1, nums[0])
        # for x in range(len(nums)-1):
        #     if(nums[x+1]-nums[x] > 1):
        #         disappeared += range(nums[x]+1, nums[x+1])
        # disappeared += range(nums[-1]+1, len(nums)+1)
        # return disappeared
                

class Solution5:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])
            
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        
        return result                

solution5 = Solution5()

res = solution5.findDisappearedNumbers([4,3,2,7,8,2,3,1])
print(res)          