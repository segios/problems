# https://leetcode.com/problems/symmetric-tree/
# 101. Symmetric Tree
# Easy
# Tree, DFS, BFS
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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionDFS:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        res = True
        if not root:
            return res
        
        left = []
        right = []

        def fillLeft(node):
            if not node:
                return
            if node.left:
                fillLeft(node.left)
            elif node.right:
                left.append(None)

            if node.right:
                fillLeft(node.right)
            elif node.left:
                left.append(None)

            left.append(node.val)

        def fillRight(node):
            if not node:
                return
            if node.right:
                fillRight(node.right)
            elif node.left:
                right.append(None)
            if node.left:
                fillRight(node.left)
            elif node.right:
                right.append(None)
            
            right.append(node.val)

        fillLeft(root.left)
        fillRight(root.right)

        return left == right

solution = SolutionDFS()

res = solution.isSymmetric(construct([1,2,2,3,4,4,3]))
#print (res) 

class TestSolutionDFS(unittest.TestCase):
    def setUp(self):
            self.solution = SolutionDFS()

    def testValid(self):
        res = solution.isSymmetric(construct([1,2,2,3,4,4,3]))
        print (res) 
        self.assertEqual(res, True)

    def testInValid(self):
        res = solution.isSymmetric(construct([1,2,2,None,3,None,3]))
        print (res) 
        self.assertEqual(res, False)     
if __name__ == '__main__':
    unittest.main()