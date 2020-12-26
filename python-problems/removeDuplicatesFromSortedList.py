# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# 83. Remove Duplicates from Sorted List
# Easy
# Linked List
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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if(head == None):
            return head
        
        node = head.next
        prev = head
        while(node != None):
            if(prev.val == node.val):
                prev.next = node.next
            else :
                prev = node
            node = node.next

        return head


solution = Solution()

res = solution.deleteDuplicates(construct([1,1,2,3,4,4,5,6]))
printList(res)
