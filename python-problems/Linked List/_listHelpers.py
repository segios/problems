from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ListNodeKey:
    def __init__(self, key=0, val=0, next=None):
        self.key = key
        self.val = val
        self.next = next        

def construct(nums: List[int]) -> ListNode:
    root = ListNode(-1)
    cur = root
    for x in nums:
        cur.next = ListNode(x)
        cur = cur.next
    return root.next

def printList (list : ListNode) :
    while list != None:
        print (list.val)
        list =  list.next


        