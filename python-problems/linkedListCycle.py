# https://leetcode.com/problems/linked-list-cycle/
# 141. Linked List Cycle
# Easy
# Linked List, Two Pointers (Fast & Slow Pointers)
# B
# Floyd's Tortoise and Hare https://www.youtube.com/watch?v=pKO9UjSeLew

from typing import List
from _listHelpers import *

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        map = {}
        cur = head

        while cur != None:
            if cur in map:
                return True
            map[cur] = 1
            cur = cur.next

        return False


solution = Solution()

res = solution.hasCycle(construct([-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]))
print (res)