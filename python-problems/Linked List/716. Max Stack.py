# https://leetcode.com/problems/max-stack/
# 716. Max Stack
# Easy
# Linked List, Stack, Design, Doubly-Linked List, Ordered Set
# 


from typing import List
from _listHelpers import *
from collections import OrderedDict, deque

class TreeNode:
    def __init__(self, value: int = 0, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None
    
    def __add(self, x: int, node):
        if(node.val == x):
            newNode = TreeNode(x)
            if node.right:
                newNode.right = node.right
                node.right = newNode
            else:
                node.right = newNode

        if(node.val < x):
            if node.right:
                self.__add(x, node.right)
            else:
                node.right = TreeNode(x)
        else:
            if node.left:
                self.__add(x, node.left)
            else:
                node.left = TreeNode(x)

    def add(self, x: int):
        if(not self.root):
            self.root = TreeNode(x)
            return
        
        self.__add(x, self.root) 

    def __remove(self, x: int, node):
        if(node.val == x):
            if node.right:

        if(node.val <= x):
            if node.right:
                self.__add(x, node.right)
            else:
                node.right = TreeNode(x)
        else:
            if node.left:
                self.__add(x, node.left)
            else:
                node.left = TreeNode(x)

    def remove(self, x: int):
        if(not self.root):
            return
        
        self.__remove(x, self.root) 

class MaxStack:

    def __init__(self):
        self.dic = deque()
        self.root = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def push(self, x: int) -> None:

        node = Node(x) 
        node.prev = self.tail.prev
        node.next = self.tail



        self.tail.prev.next = node
        self.tail.prev = node

        self.dic[x] = x


    def pop(self) -> int:
        

    def top(self) -> int:
        

    def peekMax(self) -> int:
        

    def popMax(self) -> int:
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

solution = MaxStack()

