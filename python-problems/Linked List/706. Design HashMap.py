# https://leetcode.com/problems/design-hashmap/
# 706. Design HashMap
# Easy
# Array, Linked List
# A/B


from typing import List
from _listHelpers import *
from collections import OrderedDict, deque

class MyHashMapModulo:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.arr = [None] * 1000
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash = key % 1000

        newNode = ListNodeKey(key, value)
        if not self.arr[hash]:
            self.arr[hash] = newNode
        else:
            node = self.arr[hash]
            while node and node.key != key:
                node = node.next
            
            if node:
                node.val = value
            else:
                newNode.next = self.arr[hash]
                self.arr[hash] = newNode
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash = key % 1000
        if self.arr[hash] == None:
            return -1
        node = self.arr[hash]
        while node and node.key != key:
            node = node.next
        if node:
            return node.val
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash = key % 1000
        if self.arr[hash] == None:
            return 
        node = self.arr[hash]
        prev = None
        while node and node.key != key:
            prev = node
            node = node.next
        if node:
            if prev:
                prev.next = node.next
            else:
                self.arr[hash] = node.next
        

class MyHashMapArray:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [None] * 1000001
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.arr[key] = value
        # if not self.arr:
        #     self.arr[key] = ListNode(value)
        # else:

        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if self.arr[key] == None:
            return -1
        return self.arr[key]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.arr[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

solution = MyHashMap()

# ["MyHashMap","remove","put","put","put","put","put","put","get","put","put"]
# [[],[2],[3,11],[4,13],[15,6],[6,15],[8,8],[11,0],[11],[1,10],[12,14]]

solution.remove(2)
solution.put(3,11)
solution.put(4,13)
solution.put(15,6)
solution.put(6,15)
solution.put(8,8)
solution.put(11,0)
solution.get(11)
solution.put(1,10)
solution.put(12,14)