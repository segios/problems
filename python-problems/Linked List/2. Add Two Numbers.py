# https://leetcode.com/problems/add-two-numbers/
# 2. Add Two Numbers
# Medium
# Linked List
# A


from typing import List
from _listHelpers import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = ListNode()
        result = node
        cl1 = l1
        cl2 = l2
        carry = 0
        while cl1 and cl2:
            val = cl1.val + cl2.val + carry
            carry = val // 10
            val = val % 10
            node.next = ListNode(val)
            node = node.next
            cl1 = cl1.next
            cl2 = cl2.next
        
        rest = cl1 if cl1 != None else cl2
        while rest:
            val = rest.val + carry
            carry = val // 10
            val = val % 10
            node.next = ListNode(val)
            node = node.next
            rest = rest.next

        if carry > 0:
            node.next = ListNode(carry)
        
        return result.next

solution = Solution()

res = solution.addTwoNumbers(construct([2,4,3]), construct([5,6,4]))
printList(res)


res = solution.addTwoNumbers(construct([0]), construct([0]))
printList(res)

res = solution.addTwoNumbers(construct([9,9,9,9,9,9,9]), construct([9,9,9,9]))
printList(res)