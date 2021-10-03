# https://leetcode.com/problems/3sum-closest/
# 16. 3Sum Closest
# Medium
# Arrays
# 

from collections import defaultdict
import sys
from typing import DefaultDict, List, Tuple

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:         


solution = Solution()

res = solution.threeSum([-1,2,1,-4], 1)
print (res)


res = solution.threeSum([0, 0, 0], 1)
print (res)




