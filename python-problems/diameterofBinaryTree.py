# https://leetcode.com/problems/diameter-of-binary-tree/
# 543. Diameter of Binary Tree
# Easy
# Tree, DFS
# 

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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0

        return res
    
solution = Solution()

tree = construct([1, 2, 3, 4, 5, None, None])
res = solution.diameterOfBinaryTree(tree)
print(res)        