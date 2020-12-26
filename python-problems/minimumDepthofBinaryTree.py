# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# 111. Minimum Depth of Binary Tree
# Easy
# Tree, BFS, DFS
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
    def minDepth(self, root: TreeNode) -> int:
        next_level = deque([root])
        len = 0
        while root and next_level:
            curr_level = next_level
            next_level = deque()
            len = len + 1

            for node in curr_level:
                if(not node.left and not node.right):
                    return len

                if(node.left):
                    next_level.append(node.left)
                if(node.right):
                    next_level.append(node.right)


        return len


class Solution1:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            node_deque = deque([(1, root),])
        
        while node_deque:
            depth, root = node_deque.popleft()
            children = [root.left, root.right]
            if not any(children):
                return depth
            for c in children:
                if c:
                    node_deque.append((depth + 1, c))        