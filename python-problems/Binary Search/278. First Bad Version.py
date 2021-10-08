# https://leetcode.com/problems/first-bad-version/
# 278. First Bad Version
# Easy
# Binary Search
# A


from typing import List

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

bad = 4

def isBadVersion(version):
    return version == bad

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n

        l, h = 0, n
        while l <= h:
            m = l + (h-l)//2
            isBad = isBadVersion(m)
            if not isBad:
                l = m + 1
            else:
                h = m - 1
        return l

solution = Solution()

bad = 4
res = solution.firstBadVersion(5)
print (res)