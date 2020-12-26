# https://leetcode.com/problems/remove-linked-list-elements/
# 203. Remove Linked List Elements
# Easy
# Linked List, Sentinel node
# A
# 

from typing import List
from _listHelpers import *

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return head

        root = head
        while root != None and root.val == val:
            root = root.next

        if(root == None):
            return root

        prev = root
        currNode = root.next

        while currNode != None:
            if currNode.val == val:
                prev.next = currNode.next
            else: 
                prev = currNode
            currNode = currNode.next
        
        return root


solution = Solution()

res = solution.removeElements(construct([6, 7,  6, 1,2,6,3,4,5,6]), 6)

printList(res)
