# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# 107. Binary Tree Level Order Traversal II
# Easy
# Tree, BFS
# A/B

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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        def traverseNodes(nodes:List[TreeNode], level, resultArr):
            nextNodes = []
            for node in nodes:
                if node:
                    if node.left:
                        nextNodes.append(node.left)
                    if node.right:
                        nextNodes.append(node.right)
            if(len(nextNodes) > 0):
                resultArr.insert(0, nextNodes)
                traverseNodes(nextNodes, level+1, resultArr)
        if root == None:
            return []
        levelNodes = [[root]]
        traverseNodes([root], 0, levelNodes)
        res = []
        for nodeArr in levelNodes:
            na = []
            for node in nodeArr:
                if node:
                    na.append(node.val)
            res.append(na)
        return res

class SolutionDFSPreorder:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
            
        helper(root, 0)
        return levels[::-1]

class SolutionBFSQueue:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levels = []
        next_level = deque([root])
        
        while root and next_level:
            curr_level = next_level
            next_level = deque()
            levels.append([])
            
            for node in curr_level:
                # append the current node value
                levels[-1].append(node.val)
                # process child nodes for the next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                    
        return levels[::-1]

solution = Solution()

#res = solution.levelOrderBottom(construct([-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]))
#print (res)        