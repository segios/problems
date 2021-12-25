# https://leetcode.com/problems/basic-calculator/
# 224. Basic Calculator
# Hard
# Math, String, Stack, Recursion
# A/B

import sys
from typing import List, Tuple
from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        def evalScope(s: str, i: int, mult: int):
            if (i >= len(s)):
                return (0, i)
            res = 0
            negate = 1
            while i < len(s):
                c = s[i]
                if c.isdigit():
                    sdigit = 0
                    while i < len(s) and c.isdigit():
                        sdigit = sdigit * 10  + int(c)
                        i += 1
                        if (i >= len(s)):
                            break
                        if not s[i].isdigit():
                            i -= 1
                            break
                        c = s[i]
                    res +=  negate * mult * sdigit
                if c == '-':
                    negate = -1 
                elif c == '+':
                    negate = 1
                elif c == '(':
                    evalRes = evalScope(s, i+1, mult * negate)
                    res += evalRes[0]
                    i = evalRes[1]
                elif c == ')':
                    return (res, i) 
                i += 1
            return (res, i) 

            
        res = evalScope(s, 0, 1)

        return res[0]


solution = Solution()

res = solution.calculate("2147483647")
print (res)


res = solution.calculate("-(21 + 3)")
print (res)

res = solution.calculate("-(-(2 + 3))")
print (res)

