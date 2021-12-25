# https://leetcode.com/problems/binary-tree-inorder-traversal/
# 94. Binary Tree Inorder Traversal
# Easy
# Stack, 
# 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import List, Optional, Tuple
from _treeHelpers import *

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stk = deque()
        
        res = []
        
        if not root:
            return res
        
        el = root
        stk.append(el)
        
        while stk:
            el = stk.popleft()
            
            if el.left:
                stk.append(el.left)

            if el.right:
                stk.append(el.right)

solution = Solution()

res = solution.inorderTraversal([4,2,2,5])
print (res)




