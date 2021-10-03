# https://leetcode.com/problems/index-pairs-of-a-string/
# 1065. Index Pairs of a String
# Easy
# Trie, String
#  

from typing import List
from collections import deque
import itertools 


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:

        
solution = Solution()

res = solution.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"])
print (res)

