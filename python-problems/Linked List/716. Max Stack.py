# https://leetcode.com/problems/max-stack/
# 716. Max Stack
# Easy
# Linked List, Stack, Design, Doubly-Linked List, Ordered Set
# B/C

from typing import List
from _listHelpers import *
from collections import OrderedDict, deque


# first, #155 Min Stack is an easy problem but this one is definately NOT easy (at least for getting the optimized O(logN) solution). The different between this problem and #155 is at the popMax function: it requires to remove an element in the middle of the list and also to find the next max. So doubly linked list and heap are the best data structure for these two requirement.
class Node:
    def __init__(self, val = 0):
        self.next = None
        self.prev = None
        self.val = val

class MaxStackHeap:

    def __init__(self):
		# O(1)
        """
        initialize your data structure here.
        """
        # create a dummy node for doubly linked list. This doubly linked list will be used to save the element in the order of they been pushed
        self.order_id = 0
        self.dummy = Node()
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        # create a heap to maintain the max_value on the top
        self.heap = [] # the element in heap will look like (value, order_id, node)
        self.soft_delete = set() # served as a cache for the element need to be removed from heap

    def push(self, x: int) -> None:
		# O(logN)
        self.order_id += 1
        new_node = Node(x)
        # add new node to the end of doubly linked list
        prev_node = self.dummy.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = self.dummy
        self.dummy.prev = new_node
        # add new node to heap
        heapq.heappush(self.heap, (-x, -self.order_id, new_node))

    def pop(self) -> int:
		# O(1)
        node_to_remove = self.dummy.prev
        # remove it from doubly linked list
        self.remove_node_from_doubly_linked_list(node_to_remove)
        # add this node to soft delete set, later when we see the top of heap is this node, we remove it
        self.soft_delete.add(node_to_remove)
        return node_to_remove.val
        
    def top(self) -> int:
		# O(1)
        return self.dummy.prev.val

    def peekMax(self) -> int:
		# O(k*logN), k is the elements in self.soft_delete. Amortized O(logN)
        while self.heap[0][2] in self.soft_delete:
            self.soft_delete.remove(heapq.heappop(self.heap)[2])
        return -self.heap[0][0]

    def popMax(self) -> int:
		# O(k*logN), k is the elements in self.soft_delete. Amortized O(logN)
        while self.heap[0][2] in self.soft_delete:
            self.soft_delete.remove(heapq.heappop(self.heap)[2])
        node_to_remove = heapq.heappop(self.heap)[2]
        # remove it from doubly linked list
        self.remove_node_from_doubly_linked_list(node_to_remove)
        return node_to_remove.val

    def remove_node_from_doubly_linked_list(self, node):
		# this is a helper function, O(1)
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

from sortedcontainers import SortedDict

class Dllnode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class dll:
    def __init__(self):
        self.head = Dllnode(0)
        self.tail = Dllnode(0)
        self.head.next = self.tail
        self.tail.prev = self.head 
        self.curr = self.head 
    
    def add(self, val): # adding to the tail.
        node = Dllnode(val)
        node.next = self.tail
        node.prev = self.tail.prev 
        self.tail.prev.next = node
        self.tail.prev = node
        return node
    
    def remove(self, node): # remove any given node. 
        node.prev.next = node.next
        node.next.prev = node.prev 
        return node 
        
class MaxStack:

    def __init__(self):
        self.map = SortedDict()
        self.dll = dll()

    def push(self, x: int) -> None:
        node = self.dll.add(x)
        if x not in self.map:
            self.map[x] = []
        self.map[x].append(node)

    def pop(self) -> int:
        node = self.dll.tail.prev 
        self.dll.remove(node)
        self.map[node.val].pop()
        if len(self.map[node.val]) == 0:
            del self.map[node.val]
        
        return node.val 

    def top(self) -> int:
        return self.dll.tail.prev.val 

    def peekMax(self) -> int:
        return self.map.peekitem()[0]

    def popMax(self) -> int:
        highest, addresses = self.map.peekitem()
        self.dll.remove(addresses.pop())
        if not addresses:
            self.map.popitem()
        return highest 


class MaxStack1:

    def __init__(self):
        self.stk = deque()

    def push(self, x: int) -> None:
        lastMax = x
        if self.stk:
            lastMax = max(x,self.stk[-1][1])
        self.stk.append((x, lastMax))
            

    def pop(self) -> int:
        if self.stk:
            return self.stk.pop()[0]
        return None

    def top(self) -> int:
        if self.stk:
            return self.stk[-1][0]
        return None

    def peekMax(self) -> int:
        if self.stk:
            return self.stk[-1][1]
        return None

    def popMax(self) -> int:
        tmp = []
        if not self.stk:
            return None
        lastMax = self.stk[-1][1]
        while self.stk and self.stk[-1][0] != lastMax:
            tmp.append(self.stk.pop())
        
        maxEl = self.stk.pop()
        
        for el in reversed(tmp):
           
            self.push(el[0])
        
        return maxEl[0]



# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
obj = MaxStack()

obj.push(5)
obj.push(1)
obj.push(-5)

param_5 = obj.popMax()
param_5 = obj.popMax()
param_3 = obj.top()

