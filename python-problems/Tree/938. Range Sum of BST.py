# https://leetcode.com/problems/range-sum-of-bst/
# 938. Range Sum of BST
# Easy
# Tree, Binary Search Tree, BFS, DFS
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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0
        
        if not root:
            return sum

        def checkNode(node: TreeNode):
            localSum = 0
            if low <= node.val <= high:
                localSum += node.val
                if node.left:
                    localSum += checkNode(node.left)
                if node.right:
                    localSum += checkNode(node.right)

            elif node.val < high:
                if node.right:
                    localSum += checkNode(node.right)

            elif node.val > low:
                if node.left:
                    localSum += checkNode(node.left)
            return localSum
        sum += checkNode(root)
        return sum

solution = Solution()

res = solution.rangeSumBST(construct([10,5,15,3,7,None,18]), 7, 15)
print (res) 

# class TestSolutionDFS(unittest.TestCase):
#     def setUp(self):
#             self.solution = Solution()

#     def testValid(self):
#         res = solution.isSymmetric(construct([1,2,2,3,4,4,3]))
#         print (res) 
#         self.assertEqual(res, True)

#     def testInValid(self):
#         res = solution.isSymmetric(construct([1,2,2,None,3,None,3]))
#         print (res) 
#         self.assertEqual(res, False)     
# if __name__ == '__main__':
#     unittest.main()