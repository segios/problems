# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# 744. Find Smallest Letter Greater Than Target
# Easy
# Binary Search
# A/B (look)
# 


from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, m = 0, len(letters) -1 
        
        if(letters[len(letters) -1 ] < target):
            return letters[0]

        while l <= m and m < len(letters):
            mid = l + ((m - l) // 2)
            if letters[mid] == target:
                l = mid+1
                if(l > m): 
                    m=m+1
            elif letters[mid] < target:
                l = mid+1
            elif (m-l) == 1 or letters[mid-1] <= target:
                return letters[mid]
            else:
                m = mid -1 

        return  letters[0]

class Solution1(object):
    def nextGreatestLetter(self, letters, target):
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]


# class Solution {
#     public char nextGreatestLetter(char[] letters, char target) {
#         int lo = 0, hi = letters.length;
#         while (lo < hi) {
#             int mi = lo + (hi - lo) / 2;
#             if (letters[mi] <= target) lo = mi + 1;
#             else hi = mi;
#         }
#         return letters[lo % letters.length];
#     }
# }

solution = Solution()

res = solution.nextGreatestLetter(["c", "f", "j"], "c")
print(res) 

res = solution.nextGreatestLetter(["c", "f", "j"], "d")
print(res) 

res = solution.nextGreatestLetter(["a", "b"], "z")
print(res) 

res = solution.nextGreatestLetter(["c", "f", "j"], "a")
print(res) 


res = solution.nextGreatestLetter(["c", "f", "j"], "j")
print(res) 

res = solution.nextGreatestLetter(["c", "f", "j"], "k")
print(res) 