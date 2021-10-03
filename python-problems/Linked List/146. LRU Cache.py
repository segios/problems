# https://leetcode.com/problems/lru-cache/
# 146. LRU Cache
# Medium
# Linked List
# A/B


from typing import List
from _listHelpers import *

class Node:
    def __init__(self, key: int = 0, value: int = 0, next = None, prev = None):
        self.key = key
        self.val = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.storage = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def rearrangeNode(self, newNode):
        if newNode.next is not None:
            prevNode = newNode.prev
            newNode.next.prev = prevNode
            prevNode.next = newNode.next

        newNode.next = self.head.next
        self.head.next = newNode
        newNode.next.prev = newNode
        newNode.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.storage:
            return -1
        
        node = self.storage[key]
        self.rearrangeNode(node)

        return node.val

    def put(self, key: int, value: int) -> None:


            

        if key in self.storage:
            node = self.storage[key]
            node.val = value
            self.rearrangeNode(node)
            return

        if len(self.storage) >= self.capacity:
            if self.tail.prev != self.head:
                nodeToDel = self.tail.prev
                nodeToDel.prev.next = self.tail
                self.tail.prev = nodeToDel.prev
                del self.storage[nodeToDel.key]
        

        newNode = Node(key, value)
        self.rearrangeNode(newNode)
        self.storage[key] = newNode


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

["LRUCache","put","put","put","put","get","get"]
[[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
obj = LRUCache(2)
obj.put(2,1)
obj.put(1,1)
obj.put(2,3)
obj.put(4,1)
param_1 = obj.get(1)
print (param_1)

param_1 = obj.get(2)
print (param_1)

print ("-------------------------------")
#["LRUCache","put","put","get","put","get","put","get","get","get"]
#[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
param_1 = obj.get(1)
print (param_1)
obj.put(3,3)
param_1 = obj.get(2)
print (param_1)
obj.put(4,4)
param_1 = obj.get(1)
print (param_1)
param_1 = obj.get(3)
print (param_1)
param_1 = obj.get(4)
print (param_1)

print ("-------------------------------")
# ["LRUCache","get","put","get","put","put","get","get"]
# [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
obj = LRUCache(2)
param_1 = obj.get(2)
print (param_1)
obj.put(2,6)
param_1 = obj.get(1)
print (param_1)
obj.put(1,5)
obj.put(1,2)
param_1 = obj.get(1)
print (param_1)
param_1 = obj.get(2)
print (param_1)
