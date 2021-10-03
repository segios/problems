# https://leetcode.com/problems/trapping-rain-water/
# 42. Trapping Rain Water
# Hard
# Arrays
# 

import sys
from typing import List, Tuple

class Solution:
    def trap(self, height: List[int]) -> int:
        stk = []
        res = 0
        for i , h in enumerate(height):
            if len(stk) == 0:
                stk.append((h, 0))
                continue

            (fh, fv) = stk[0] 
            (lh, lv) = stk[len(stk) - 1] 
            if h <= lh:
                stk.append((h, fh - h))
            else:
                (lh, lv) = stk.pop()
                idx = len(stk)-1
                while idx >= 0 and lh < h:
                    diff = h - lh
                    vol = min (lv, diff)
                    res += vol
                    if(lv - diff > 0):
                        stk.append((lh, lv - diff))
                        (lh, lv) = stk[idx] 
                    else:
                        (lh, lv) = stk.pop()
                    idx -= 1
                    
                stk.append((h, 0))
        return res        
            


class Solution2:
    def trap(self, height: List[int]) -> int:
        volume = 0
        arr = height
        while len(arr) > 1:
            (vol, arr) = self.trim(arr)
            volume += vol
            for i in range(len(arr)):
                arr[i] -= 1

        return volume
    def trim(self, arr: List[int]):
        res = 0
        if len(arr) <= 1:
            return (res, arr)
        
        for i , h in enumerate(arr):
            if (h < 0):
                res += abs(h)
                continue
            if h == 0:
                continue
            if(i+1 >= len(arr) ):
                break
            if(arr[i+1] < h):
                break
        arr = arr[i:]
        for i, h in reversed(list(enumerate(arr))):
            if (h < 0):
                res += abs(h)
                continue
            if h == 0:
                continue
            if(i-1 <= 0 ):
                break
            if(arr[i-1] < h):
                break
        arr = arr[:i+1]

        return (res, arr)
        

class Solution1:
    def trap(self, height: List[int]) -> int:
        volume = 0
        walls = []
        holes = []
        for i, h in enumerate(height):
            wallLens = len(walls)
            if wallLens > 0:
                lastH = walls[wallLens-1]
                if lastH >= h:
                    diff = lastH - h
                    for wi, w in reversed(list(enumerate(walls))):
                        if w >= h:
                            if(holes[wi] > 0):
                                holes[wi] += diff
                        else:
                            break
                    walls.append(h)  
                    holes.append(diff)
                else:
                    diff = h - lastH
                    for wi, w in reversed(list(enumerate(walls))):
                        if w < h:
                            if(holes[wi] > 0):
                                currVolume = min (holes[wi], diff)
                                volume += currVolume
                                holes[wi] -= currVolume
                        else:
                            lastH = walls[len(walls)-1]
                            diff = h - lastH
                            walls.append(h)  
                            holes.append(diff)
                            break

            elif h > 0:
                walls.append(h)
                holes.append(-1)
        return volume


solution = Solution()

res = solution.trap([0,1,0,2])
print (res)

res = solution.trap([2,1,0,1,3])
print (res)

res = solution.trap([4,2,0,3,2,5])
print (res)

res = solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print (res)





