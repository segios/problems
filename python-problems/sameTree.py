# https://leetcode.com/problems/same-tree/
# 100. Same Tree
# Easy
# Tree, DFS
# A

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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if(not p and not q):
            return True
        
        stack = deque([(p, q)])

        
        while stack:

            pnode, qnode = stack.popleft()

            if(pnode and not qnode or not pnode and qnode):
                return False

            if pnode.val != qnode.val:
                return False

            if pnode.left or qnode.left :
                stack.append((pnode.left, qnode.left))

            if pnode.right or qnode.right :
                stack.append((pnode.right, qnode.right))
        
        
        return True


solution = Solution()

res = solution.isSameTree(TreeNode(1), TreeNode(1, None, TreeNode(2)))
print(res)



class Solution1:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """    
        def check(p, q):
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True
        
        deq = deque([(p, q),])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False
            
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
                    
        return True