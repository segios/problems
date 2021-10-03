# https://leetcode.com/problems/generate-parentheses/
# 22. Generate Parentheses
# Medium
# String, Backtracking
# B
# 

from typing import List
from collections import Counter


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def generate(start: int, res: List[str]):
            if(start == n):
                return

            res.append('(')
            generate(start+1,  res)
            res.append(')')

        currentStart = ""
        for i in range(n):
            res = []
            generate(i, res)
            output.append(currentStart + "".join(res) )
            currentStart += "()"
        
        return  output

solution = Solution()
res = solution.generateParenthesis(3)
print(res)    