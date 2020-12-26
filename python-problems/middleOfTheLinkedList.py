# https://leetcode.com/problems/middle-of-the-linked-list/
# 876. Middle of the Linked List
# Easy
# Linked List, Two Pointers (Fast & Slow Pointers)
# A/B
# 

from typing import List
from _listHelpers import *

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        node = head
        nodes = []
        while node != None:
            nodes.append(node)
            node = node.next

        idx = len(nodes) // 2

        return nodes[idx]

class SolutionFastPointers(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

solution = Solution()

res = solution.middleNode(construct([1,2,3,4,5]))
printList(res)
