from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct(tree: List[int]) -> TreeNode:
    if(len(tree)) == 0:
        return None

    root = TreeNode(tree[0])
    currentLevel = deque([root])
    
    def fillLevel(que : deque, idx, tree: List[int]):
        nextLevel = deque()
        
        if len(tree) <= idx:
            return

        while que:
            node : TreeNode = que.popleft()
            if tree[idx]:
                node.left = TreeNode(tree[idx])
                nextLevel.append(node.left)

            idx = idx + 1
            if tree[idx]:
                node.right = TreeNode(tree[idx])
                nextLevel.append(node.right)
            idx = idx + 1
        
        fillLevel(nextLevel, idx, tree)

    fillLevel(currentLevel, 1, tree)
    return root

    # cur = root
    # x = 0
    # level = 0
    # while x < len(nums):
    #     cur.val = nums[x]

    #     cur.next = TreeNode(x)
    #     cur = cur.next
    # return root.next

def printTree (tree : TreeNode) :
        if tree:
            print(tree.val)
            printTree (tree.left)
            printTree (tree.right)

