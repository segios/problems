# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# 1290. Convert Binary Number in a Linked List to Integer
# Easy
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
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        
        while head :
            result = (result << 1) + head.val
            head = head.next
            
        return result

solution = Solution()

res = solution.addTwoNumbers(construct([1,0,1]))
printList(res)

