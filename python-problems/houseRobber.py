# https://leetcode.com/problems/house-robber/
# 198. House Robber
# Easy
# Dynamic Programming
# C 
# https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/tutorial/

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        if(len(nums) == 0):
            return 0

        if(len(nums) == 1):
            return nums[0]

        dp[0] = nums[0]
        dp[1] = nums[1]

        for x in range(2, len(nums)):
            maxV = 0
            for d in range(0, x-1):
                if(maxV < dp[d]):
                    maxV = dp[d]
            dp[x] = nums[x] + maxV
        
        return max(dp)

# public int rob(int[] num) {
#     int prevMax = 0;
#     int currMax = 0;
#     for (int x : num) {
#         int temp = currMax;
#         currMax = Math.max(prevMax + x, currMax);
#         prevMax = temp;
#     }
#     return currMax;
# }


class Solution1:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return max(dp)

solution = Solution()

res = solution.rob([2,1,1,2])
print (res)

res = solution.rob([2,7,9,3,1])
print (res)


