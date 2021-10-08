# https://leetcode.com/problems/max-stack/
# 716. Max Stack
# Easy
# Linked List, Stack, Design, Doubly-Linked List, Ordered Set
# 


from typing import List
from _listHelpers import *
from collections import OrderedDict, deque
import heapq

class Item:
    def __init__(self, val: int, ref = None):
        self.val = val
        self.ref = ref
    def __lt__(self, other):    
        return self.val < other.val

class MaxStack:

    def __init__(self):
        self.stack = deque()
        self.heapData = []
        heapq.heapify(self.heapData)

    def heapPush(self, item):
        heapq.heappush(self.heapData, item)

    def heapPop(self):
        return heapq.heappush(self.heapData)

    def heapPeek(self):
        if len(self.heapData) == 0:
            return None
        return self.heapData[0]

    def push(self, x: int) -> None:
        item = Item(x)
        itemHeap = Item(x)
        item.ref = itemHeap
        itemHeap.ref = item

        self.stack.append(item)
        self.heapPush(itemHeap)
            
    def pop(self) -> int:
        if len(self.stack)  > 0:
            it = self.stack.pop()
            # remove from heap
            #self.removeFromheap(it.ref)
            return it.val
        return None

    def top(self) -> int:
        if len(self.stack)  > 0:
            it = self.stack.pop()
            self.stack.append(it)
            return it.val
        return None

    def peekMax(self) -> int:
        if len(self.stack)  == 0:
            return None
        it = self.heapPeek()
        return  it.val

    def popMax(self) -> int:
        it = self.heapPop()
        self.stack.remove(it.ref)
        return  it.val


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
obj.push(3)

param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.peekMax()
param_5 = obj.popMax()
param_5 = obj.popMax()
