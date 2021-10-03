# https://leetcode.com/problems/spiral-matrix/
# 54. Spiral Matrix
# Medium
# Arrays
# B
# 

from typing import List
from collections import Counter

class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans


class Solution(object):
    def spiralOrder(self, matrix):
        def spiral_coords(r1, c1, r2, c2):
            for c in range(c1, c2 + 1):
                yield r1, c
            for r in range(r1 + 1, r2 + 1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1

        if not matrix: return []
        ans = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for r, c in spiral_coords(r1, c1, r2, c2):
                ans.append(matrix[r][c])
            r1 += 1; r2 -= 1
            c1 += 1; c2 -= 1
        return ans


class Solution1:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        startx, starty = 0, 0
        boundx = len(matrix[0])
        boundy = len(matrix)
        res = []
        posx, posy = 0,0

        if boundx == 1:
            for i in range(boundy):
               res.append(matrix[i][0]) 
            return res

        if boundy == 1:
            for i in range(boundx):
               res.append(matrix[0][i]) 
            return res

        while startx < boundx or starty < boundy:
            for i in range(startx, boundx):
                res.append(matrix[posy][posx])
                posx += 1
            
            posx -= 1
            starty += 1
            posy += 1

            if startx > boundx or starty > boundy:
                break

            for j in range(starty, boundy):
                res.append(matrix[posy][posx])
                posy+=1
            
            posy -=1
            boundx-=1
            posx -= 1

            if startx > boundx or starty > boundy:
                break

            for i in range(boundx, startx, -1):
                res.append(matrix[posy][posx])
                posx-=1
            
            posx+=1
            boundy-=1
            posy -=1

            if startx > boundx or starty > boundy:
                break

            for j in range(boundy, starty, -1):
                res.append(matrix[posy][posx])
                posy-=1

            posy +=1
            boundy -=1
            startx +=1
            posx += 1

            if startx > boundx or starty > boundy:
                break

        return res

solution = Solution()

m = [[1,2,3],[4,5,6],[7,8,9]]
res = solution.spiralOrder(m)
print(res)    