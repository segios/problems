# https://leetcode.com/problems/find-anagram-mappings/
# 760. Find Anagram Mappings
# Easy
# Strings, HashTable, Sorting
# A

import sys
from typing import List
from collections import Counter, defaultdict

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {x : i for i, x in enumerate(nums2)}

        res = []
        for v in nums1:
            res.append(dic[v])
        return res

class SolutionS:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = defaultdict(list)
        for i, v in enumerate(nums2):
            dic[v].append(i)
        
        res = []
        for v in nums1:
            x = dic[v].pop()
            res.append(x)
        return res
        

solution = Solution()

res = solution.anagramMappings([12,28,46,32,50], [50,12,32,46,28])
print (res)
