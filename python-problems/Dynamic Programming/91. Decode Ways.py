# https://leetcode.com/problems/decode-ways/
# 91. Decode Ways
# Medium
# String, Dynamic Programming
# C

import sys
from typing import List
import math

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 1

        for i in range (1, len(s)):
            if s[i] != '0':
                dp[i+1] += dp[i]
            
            num = int(s[i-1:i+1])
            if 10 <= num <= 26:
                dp[i+1] += dp[i-1] 

        return dp[-1]

       
class SolutionRec:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        data: List[str] = list(s)
        memo = {}

        def isCanBeDecoded(data: List[str], startIdx, length):
            num = 0
            if data[startIdx] == '0':
                return False
            if length == 1:
                if startIdx + 1 < len(data):
                    if data[startIdx+1] == '0':
                        return False        
                return True

            if startIdx + 1 < len(data):
                num = int(data[startIdx]) * 10 + int(data[startIdx+1])
                if num <= 26 :
                    return True
            return False

        def recursive (index, data):
            if index in memo:
                return memo[index]

            if index == len(data):
                return 1

            if data[index] == '0':
                return 0

            if index == len(data)-1:
                return 1

            ans = recursive (index + 1, data)
            if isCanBeDecoded(data, index, 2):
                ans += recursive (index + 2, data)

            memo[index] = ans
            return ans

        return recursive (0, data)

solution = Solution()

res = solution.numDecodings("226")
print (res)

res = solution.numDecodings("12")
print (res)


solution2 = SolutionRec()

res = solution2.numDecodings("226")
print (res)

res = solution2.numDecodings("12")
print (res)



