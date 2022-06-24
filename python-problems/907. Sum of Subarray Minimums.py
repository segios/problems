
from typing import List

class Solution:
    def   sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        curMin = 0
        maxRes = 10**9+7
        for i in range(len(arr)):
            curMin = arr[i]
            for j in range (i, len(arr)):
                curMin = min (curMin, arr[j])
                res += curMin
                res %= maxRes
                
        return res



solution = Solution()

res = solution.sumSubarrayMins([3,1,2,4])
print(res)