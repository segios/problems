# https://leetcode.com/problems/number-of-islands/
# 200. Number of Islands
# Medium
# Arrays
# A

import sys
from typing import List, Tuple

#bfs
class Solution: 
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        


class SolutionDfs:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        def markIsland(x,y, grid):
            grid[y][x] = 's'
            if y+1 < len(grid) and grid[y+1][x] == '1':
                 markIsland(x,y+1, grid)
            if y-1 >= 0 and grid[y-1][x] == '1':
                 markIsland(x,y-1, grid)
            if x+1 < len(grid[0]) and grid[y][x+1] == '1':
                markIsland(x+1,y, grid)
            if x-1 >=0 and grid[y][x-1] == '1':
                markIsland(x-1,y, grid)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    markIsland(j, i, grid)
        return res

solution = Solution()
grid = [["1","1","1"],
        ["0","1","0"],
        ["1","1","1"]]
res = solution.numIslands(grid)
print (res)


grid = [["1","0","1","1","0","1","1"]]
res = solution.numIslands(grid)
print (res)

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

res = solution.numIslands(grid)
print (res)

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

res = solution.numIslands(grid)
print (res)







