# https://leetcode.com/problems/squares-of-a-sorted-array/
# 977. Squares of a Sorted Array
# Easy
# Arrays, Two Pointers
# A

from typing import List

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res: List[int] = []
        positiveIdx = -1
        x = 0
        while x < len(A):
            if A[x] < 0:
                positiveIdx = positiveIdx + 1
                x = x + 1
            else:
                if positiveIdx >= 0: 
                    if A[x] * A[x] <  A[positiveIdx] * A[positiveIdx]:
                        res.append(A[x] * A[x])
                        x = x + 1
                    else:
                        res.append(A[positiveIdx] * A[positiveIdx])
                        positiveIdx = positiveIdx - 1
                else:
                    res.append(A[x] * A[x])
                    x = x + 1
        
        while positiveIdx >= 0:
            res.append(A[positiveIdx] * A[positiveIdx])
            positiveIdx = positiveIdx - 1

        return res


solution = Solution()

res = solution.sortedSquares([-4,-1,0,3,10])
print (res)
