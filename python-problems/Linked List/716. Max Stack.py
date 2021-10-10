# https://leetcode.com/problems/max-stack/
# 716. Max Stack
# Easy
# Linked List, Stack, Design, Doubly-Linked List, Ordered Set
# B/C


from typing import List
from _listHelpers import *
from collections import OrderedDict, deque

class MaxStack:

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

