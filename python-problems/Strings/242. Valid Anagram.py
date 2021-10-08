# https://leetcode.com/problems/valid-anagram/
# 242. Valid Anagram
# Easy
# Strings, HashTable, Sorting
# A

import sys
from typing import List
from collections import Counter, defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
