# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stk = []

        len = 0
        node = head
        if not head:
            return 0
        while node:
            len += 1
            node = node.next
        
        half = len // 2
        node = head
        for i in range (half):
            stk.append(node)
            node = node.next
        sum = 0
        for i in range (half):
            savedNode = stk.pop()
            
            newSum = savedNode.val + node.val
            if newSum > sum:
                sum = newSum
            node = node.next
        return sum

solution = pairSum()

res = solution.kthFactor1(24, 6)
print(res)