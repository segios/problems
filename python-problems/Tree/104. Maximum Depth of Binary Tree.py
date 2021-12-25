# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# 104. Maximum Depth of Binary Tree
# Easy
# Tree, Binary Tree, BFS, DFS
# A

from typing import List, Optional
from collections import deque
from _treeHelpers import *
import unittest

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        currentPath = 0
        
        def dfs(node, path):
            if not node:
                return path-1
            
            leftpath = dfs(node.left, path+1)
            rightpath = dfs(node.right, path+1)
            
            return max(leftpath, rightpath)
        
        return dfs(root, currentPath+1)


solution = Solution()

res = solution.maxDepth(construct([3,9,20,None,None,15,7]))
print (res) 

