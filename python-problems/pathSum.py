# https://leetcode.com/problems/path-sum/
# 112. Path Sum
# Easy
# Tree, DFS
#  A

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
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if not root:
            return False

        stack = deque([(root, sum)])

        while stack:
            node, subSum = stack.pop()
            subSum = subSum - node.val 
            if not node.left and not node.right and subSum == 0:
                return True

            if node.left:
                stack.append((node.left, subSum))

            if node.right:
                stack.append((node.right, subSum))

        return False


class SolutionRecursive:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if not root:
            return False

        subSum = sum - root.val

        if not root.left and not root.right:
            return subSum == 0

        res = False
        if root.left:
            res = self.hasPathSum(root.left, subSum)

        if res: 
            return True

        if root.right:
            res = self.hasPathSum(root.right, subSum)

        return res


solution = Solution()

tree = construct([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
res = solution.hasPathSum(tree, 22)
print(res)

tree = construct([-2, None, -3])
res = solution.hasPathSum(tree, -5)
print(res)