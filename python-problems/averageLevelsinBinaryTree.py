# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# 637. Average of Levels in Binary Tree
# Easy
# Tree, BFS
# A

from typing import List
from collections import deque
from _treeHelpers import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        avgList = []
        next_level = deque([root])
        
        while root and next_level:
            curr_level = next_level
            next_level = deque()
            level_vals = []
            
            for node in curr_level:
                # append the current node value
                level_vals.append(node.val)
                # process child nodes for the next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
        
            avgList.append(sum(level_vals) / len(level_vals))
        return avgList