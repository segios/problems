# https://leetcode.com/problems/intersection-of-two-linked-lists/
# 160. Intersection of Two Linked Lists
# Easy
# Linked List
# A/B


from typing import List
from _listHelpers import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if (not headA) or not headB:
            return None

        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA

        return p1


class SolutionHT:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        dic = {}
        if (not headA) or not headB:
            return None
        
        node = headA
        while node:
            dic[node] = 1
            node = node.next
            
        node = headB
        while node and node not in dic:
            node = node.next
            
        return node

solution = Solution()

res = solution.getIntersectionNode(construct([4,1,8,4,5]), construct([5,6,1,8,4,5]))
printList(res)

