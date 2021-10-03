# https://leetcode.com/problems/3sum/
# 15. 3Sum
# Medium
# Arrays
# C/B

from collections import defaultdict
import sys
from typing import DefaultDict, List, Tuple

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res

class Solution2p:
    def twoSum(self, nums: List[int],  i, res: List[List[int]] ) -> List[List[int]]:
        left, right = i + 1, len(nums) -1
        while(left < right):
            a = nums[left]
            b = nums[right]
            s = a + b + nums[i]
            if s > 0:
                right -= 1
            elif s < 0:
                left += 1
            else:
                res.append([nums[i], a, b])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1

        return []

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        if(nums is None or len(nums) < 3):
            return res
        
        nums.sort()

        for i in range(len(nums)):
            if(nums[i] > 0):
                break
            target = nums[i]
            if (i > 0 and target == nums[i-1]):
                continue
            self.twoSum(nums, i, res) 

        return res                


class SolutionBS:
    def find_index(self, elements, value, left, right):

        while left <= right:
            middle = (left + right) // 2

            if elements[middle] == value:
                return middle

            if elements[middle] < value:
                left = middle + 1
            elif elements[middle] > value:
                right = middle - 1
        return -1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        if(nums is None or len(nums) < 3):
            return res
        
        nums.sort()

        leftIndex = 0
        rightIndex = len(nums) - 1

        while nums[leftIndex] <= 0 and rightIndex - leftIndex > 1:
            x = nums[leftIndex]
            rightIndex = len(nums) - 1

            while(rightIndex - leftIndex > 1):
                y = nums[rightIndex]
                sum = x + y 
                z = 0 - sum

                if z > y or z > nums[rightIndex-1]:
                    break

                zIdx = self.find_index(nums, z, leftIndex+1, rightIndex-1)
                if zIdx > 0:
                    el = [e for e in res if e[0] == x and e[1] == y and e[2] == z]
                    if len(el) == 0:
                        res.append([x, y, z])
                rightIndex -= 1
            leftIndex += 1

        return res                


solution = Solution()

res = solution.threeSum([-2,0,0,2,2])
print (res)


res = solution.threeSum([-1,0,1,2,-1,-4])
print (res)

res = solution.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4])
print (res)


res = solution.threeSum([0, 0, 0, 0])
print (res)



res = solution.threeSum([])
print (res)

res = solution.threeSum([0])
print (res)











