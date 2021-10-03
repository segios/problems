# https://leetcode.com/problems/backspace-string-compare/
# 844. Backspace String Compare
# Easy
# Stack, Two Pointers
# A/B

from typing import List
from collections import deque
import itertools 

class Solution1:
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        si, ti = len(S)-1, len(T)-1
        skipS, skipT = 0, 0
        while si >= 0 or ti >= 0:
            while si >= 0:
                if (S[si] == "#"):
                    skipS += 1
                elif skipS > 0:
                    skipS -= 1
                else:
                    break
                si -= 1  
            
            while ti >= 0:
                if (T[ti] == "#"):
                    skipT += 1
                elif skipT > 0:
                    skipT -= 1
                else:
                    break
                ti -= 1  
            if si >= 0 and ti >= 0 and S[si]!=T[ti]:
                return False
            if  (si >= 0 ) != (ti >= 0):
                return False
            si -= 1
            ti -= 1  
        return True

        




class SolutionStack:
    def backspaceCompare(self, S: str, T: str) -> bool:
        si, ti = 0, 0

        rsq = deque()
        rtq = deque()
        
        while si < len(S) and ti < len(T):
            if (S[si] == "#"):
                if rsq:
                    rsq.pop()
            else:      
                rsq.append(S[si]) 

            if (T[ti] == "#"):
                if rtq:
                    rtq.pop()
            else:      
                rtq.append(T[ti]) 

            si += 1 
            ti += 1
        
        while si < len(S) :
            if (S[si] == "#"):
                if rsq:
                    rsq.pop()
            else:      
                rsq.append(S[si]) 
            si += 1 

        while ti < len(T) :
            if (T[ti] == "#"):
                if rtq:
                    rtq.pop()
            else:      
                rtq.append(T[ti]) 
            ti += 1
        
        return list(rsq) == list(rtq) 


solution = Solution()

res = solution.backspaceCompare("ab#c", "ad#c")
print (res)

res = solution.backspaceCompare("ab##", "c#d#")
print (res)

res = solution.backspaceCompare("a##c", "#a#c")
print (res)

res = solution.backspaceCompare("a#c", "b")
print (res)





