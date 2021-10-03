# https://leetcode.com/problems/merge-intervals/
# 56. Merge Intervals
# Medium
# Arrays
# A

import sys
from typing import List

# Finally someone mentioned this. I was thinking a slightly modified version of UnionFind. We would need to create an array of size max interval number - min interval number. And also another boolean array which says that the actual index is getting used. For instance -
# if the intervals are - [1,2],[2,4],[3,4],[7,8]
# After merge, parent array is ( I started from 0 index ) - 0, 1, 1, 1, 1, 5, 6, 7, 7
# and the intervals included are marked by a boolean array (again 0 index) - F, T, T, T, T, F, F, T, T (note 0, 5 and 6 are not in the original intervals so marked as false)
# Now just iterate over the array and if the interval is included use it. In this case in the parent array, starting from index 1 to 4, all have same parents (1) and all are true. So the first interval is (1,4). Then 5 and 6 are false, so ignore it. Finally 7 and 8 have the same parent (7) so create an interval (7,8). The answer is (1,4), (7,8)

# Time complexity assuming optimized union find - O(max interval number - min interval number) - in this case O(8-1)
# Same space complexity for the 2 arrays.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if(len(intervals) == 0):
            return []
        maxInterval = max(intervals, key = lambda x: x[1])[1] + 1
        
        intervalsStart = [0 for i in range(maxInterval)]
        intervalsEnd = [0 for i in range(maxInterval)]
        
        for start, end in intervals:
            intervalsStart[start] += 1
            intervalsEnd[end] -= 1
                    
        result = []
        current = [0, 0]
        lastSum = 0
        currentSum = 0
        for i in range(len(intervalsStart)):
            start = intervalsStart[i]            
            currentSum += start            
            if(lastSum == 0 and currentSum >= 1):
                current[0] = i                
            
            lastSum = currentSum
            end = intervalsEnd[i]   
            currentSum += end 
            if(lastSum > 0 and currentSum == 0):
                current[1] = i
                result.append(current)
                current = [0, 0]            
            
            lastSum = currentSum
        
        return result

class Solution1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if(intervals  == None or len(intervals) <= 1 ):
            return intervals
        
        res = [] 
        sortedIntervals = sorted(intervals, key=lambda x:x[0])

        currentInterval = sortedIntervals[0]
        res.append(currentInterval)
        
        for i in range (1, len(sortedIntervals)):
            nextInterval = sortedIntervals[i]
            if(nextInterval[0] > currentInterval[1]):
                currentInterval = nextInterval
                res.append(currentInterval)
            elif (nextInterval[1] > currentInterval[1]):
                currentInterval[1] = nextInterval[1]

        return res


solution = Solution()

res = solution.merge([[1,4],[4,5]])
print (res)

res = solution.merge([[1,3],[2,6],[8,10],[15,18]])
print (res)

