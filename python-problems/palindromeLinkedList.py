# https://leetcode.com/problems/palindrome-linked-list/
# 234. Palindrome Linked List
# Easy
# Linked List, Two Pointers (Fast & Slow Pointers)
# A/B
# 

from typing import List
from _listHelpers import *


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        if(head == None):
            return True

        if(head.next == None):
            return True

        nodes = []
        node = head
        while node:
           nodes.append(node.val) 
           node = node.next
        
        for i in range(len(nodes) // 2):
            if nodes[i] != nodes[len(nodes)-i-1]:
                return False

        return True

solution = Solution()

res = solution.isPalindrome(construct([1,3,2,4,3,2,1]))
print (res)


res = solution.isPalindrome(construct([1,2,2,2,2,1]))
print (res)

