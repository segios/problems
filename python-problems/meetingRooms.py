# https://leetcode.com/problems/meeting-rooms/
# 252. Meeting Rooms
# Easy
# Sort, Intervals
# A
# 

from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        def sortFirst(val): 
            return val[0]  
        
        intervals.sort(key = sortFirst)  
        
        for i in range(len(intervals)-1):
            if intervals[i+1][0] < intervals[i][1]:
                return False

        return True

solution = Solution()

res = solution.canAttendMeetings([[0,30],[5,10],[15,20]])
print(res) 


res = solution.canAttendMeetings([[7,10],[2,4]])
print(res) 