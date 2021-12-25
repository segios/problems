# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# 1249. Minimum Remove to Make Valid Parentheses
# Medium
# Stack
# A

import sys
from typing import List, Tuple
from collections import deque

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = deque()
        strA = list(s)
        res = []

        for i, c in enumerate(strA):
            if c != ')' and c != '(':
                res.append(c)
            else:
                if c == '(':
                   res.append(c)
                   stk.append((c, i)) 
                else:
                    if stk:
                        res.append(c)
                        stk.pop()

#  or remove items which are in stack

        strA = res  
        res = []  
        stk.clear()

        for i, c in enumerate(reversed(strA)):
            if c != ')' and c != '(':
                res.append(c)
            else:
                if c == ')':
                   res.append(c)
                   stk.append((c, i)) 
                else:
                    if stk:
                        res.append(c)
                        stk.pop()
        strA = list(reversed(res))
        return ''.join(strA)

solution = Solution()

res = solution.minRemoveToMakeValid("lee(t(c)o)de)")
print (res)

res = solution.minRemoveToMakeValid("a)b(c)d")
print (res)

res = solution.minRemoveToMakeValid("))((")
print (res)

res = solution.minRemoveToMakeValid("(a(b(c)d)")
print (res)
