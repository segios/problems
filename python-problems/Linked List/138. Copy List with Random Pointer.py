# https://leetcode.com/problems/copy-list-with-random-pointer/
# 138. Copy List with Random Pointer
# Medium
# Linked List, HashTable
# A/B


from typing import List
from _listHelpers import *
from collections import OrderedDict, defaultdict, deque

"""
# Definition for a Node.

"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = {}

        current = head
        root = Node(-1)

        prev = root
        while current:
            if current not in dic:
                dic[current] = Node(current.val)
            
            next = dic[current]

            if current.random:
                if current.random not in dic:
                    dic[current.random] = Node(current.random.val)

                next.random = dic[current.random]

            current = current.next
            prev.next = next 
            prev = next
        
        return root.next

class Solution1:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = {}
        future = defaultdict(list)
        current = head
        root = Node(-1)

        prev = root
        while current:
            next = Node(current.val)
            prev.next = next 
            prev = next

            dic[current] = next

            if current.random:
                if current.random in dic:
                    saved = dic[current.random]
                    next.random = saved
                else:
                    future[current.random].append(next)
            if current in future:
                for saved in future[current]:
                    saved.random = next
            current = current.next
        
        return root.next
