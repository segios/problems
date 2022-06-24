from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0

      #  nums.sort()

        l, r = 0, len(nums) -1

        while (l < len(nums)):
            r = len(nums) -1
            sub = nums[l:r+1]
            prevMax, prevMin = max(sub), min(sub)
            while r > l:
              res += prevMax - prevMin
              r -= 1
              if(prevMax == nums[r+1]):
                prevMax = max(nums[l:r+1])
              if(prevMin == nums[r+1]):
                prevMin = min(nums[l:r+1])

            l += 1
        return res


s = Solution();

res = s.subArrayRanges([0])
print (res)