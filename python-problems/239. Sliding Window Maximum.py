from typing import List
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
      if(not nums):
        return []

      result = []
      h = []
      for value in nums[:k]:
        heapq.heappush(h, -value)

      

      for j in range(1, len(nums)-k+1):
        result.append(-heapq.heappop(h))
        heapq.heappush(h, -nums[j+k-1])

      result.append(-heapq.heappop(h))
      return result

class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
      if(not nums):
        return []

      result = []
      currentMax = nums[0]
      currentMaxIndex = 0

      for j in range(k):
        if currentMax < nums[j]:
          currentMax = nums[j]
          currentMaxIndex= j
      result.append(currentMax)
      
      if (len(nums) == 1):
        return result

      for i in range(1, len(nums)-k+1):
        if currentMaxIndex < i: 
          currentMax = nums[j+i]
          for j in range(k):
            if currentMax < nums[j+i]:
              currentMax = nums[j+i]
              currentMaxIndex= j+i
        if nums[i+k-1] > currentMax:
          currentMax = nums[i+k-1]

        result.append(currentMax)  

      return result
s = Solution()

res = s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)

print(res)