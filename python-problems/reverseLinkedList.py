# https://leetcode.com/problems/reverse-linked-list/
# 206. Reverse Linked List
# Easy
# Linked List
# A/B (Recursion)
# 

from typing import List
from _listHelpers import *

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        node = head
        while (node):
            tempnode = node.next
            node.next = prev
            prev = node
            node = tempnode
        return prev

class SolutionRecurse:
    def reverseList(self, head: ListNode) -> ListNode: 
        
        def unwrap(head: ListNode, deep: int)-> ListNode: 
            if(head.next == None):
                self.root = head 
                return head
            r = unwrap(head.next, deep + 1)
            r.next = head
            head.next = None
            if deep == 0 :
                return self.root
            return head

        if(head == None):
            return None
        return unwrap(head, 0)

class SolutionRecurse2:
    def reverseList(self, head: ListNode) -> ListNode: 
        if head == None or head.next == None:
            return head
        
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

# solution = Solution()

# res = solution.reverseList(construct([1,2,6,3,4,5,6]))

# while res != None:
#     print (res.val)
#     res=  res.next


solution = SolutionRecurse2()

res = solution.reverseList(construct([1,2,6,3,4,5,6]))
printList(res)
