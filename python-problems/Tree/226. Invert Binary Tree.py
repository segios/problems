# https://leetcode.com/problems/invert-binary-tree/
# 226. Invert Binary Tree
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root


        def swap (node: TreeNode):
            if not node:
                return
            node.left, node.right = node.right, node.left
            swap (node.left)
            swap (node.right)

        swap (root)
        return root


solution = Solution()

res = solution.invertTree(construct([4,2,7,1,3,6,9]))
printTree (res) 

