# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# 167. Two Sum II - Input array is sorted
# Easy
# Arrays, BinarySearch, Two pointers
# A
from typing import List

class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left , right = 0, len(numbers) -1

        while(left < right):
            a = numbers[left]
            b = numbers[right]
            s = a + b
            if (s == target):
                return [left+1, right + 1]
            if s > target:
                right -= 1
            else:
                left += 1

        return []



class SolutionBS:
    def find_index(self, numbers: List[int], target: int, left, right) -> int:
        
        while(left <= right):
            mid = (left + right) // 2

            if (numbers[mid] == target):
                return mid
            if numbers[mid] > target:
                right = mid-1
            if numbers[mid] < target:
                left = mid+1
        return -1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            t = target - numbers[i]
            idx = self.find_index(numbers, t, i+1, len(numbers)-1)
            if(idx > 0):
                return [i+1, idx+1]
        return []


solution = Solution()

res = solution.twoSum([2,7,11,15], 9)
print (res)

res = solution.twoSum([2,3,4], 6)
print (res)


res = solution.twoSum([-1,0], -1)
print (res)




