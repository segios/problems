# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# 1022. Sum of Root To Leaf Binary Numbers
# Easy
# Tree, Binary Tree, DFS
# 

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
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        res = []
        def dfs(node, n):
            if not node:
                res.append(n)
                return
            
            n = n << 1 
            n += node.val

            if node.left or node.right:
                if node.left:
                    dfs(node.left, n)
                if node.right:
                    dfs(node.right, n)
            else:
               res.append(n) 
        dfs(root, 0)

        ss = 0
        for n in res:
            ss +=n
        return ss


solution = Solution()

res = solution.sumRootToLeaf(construct([1,0,1,0,1,0,1]))
print (res) 

