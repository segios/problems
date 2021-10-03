# https://leetcode.com/problems/letter-case-permutation/
# 784. Letter Case Permutation
# Medium
# Backtracking, Bit Manipulation
# A
# 

from typing import List
from collections import Counter
import itertools

class Solution4(object):
    def letterCasePermutation(self, S):
        f = lambda x: (x.lower(), x.upper()) if x.isalpha() else x
#        print (*map(f, S))
        return list(map("".join, itertools.product(*map(f, S))))

class Solution3(object):
    def letterCasePermutation(self, S):
        B = sum(letter.isalpha() for letter in S)
        ans = []

        for bits in range(1 << B):
            b = 0
            word = []
            for letter in S:
                if letter.isalpha():
                    if (bits >> b) & 1:
                        word.append(letter.lower())
                    else:
                        word.append(letter.upper())

                    b += 1
                else:
                    word.append(letter)

            ans.append("".join(word))
        return ans

class Solution2:
    def letterCasePermutation(self, S):
        ans = [[]]

        for char in S:
            n = len(ans)
            if char.isalpha():
                for i in range(n):
                    ans.append(ans[i][:])
                    ans[i].append(char.lower())
                    ans[n+i].append(char.upper())
            else:
                for i in range(n):
                    ans[i].append(char)

        return map("".join, ans)

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        self.res = []
        def helper(ss:List[str], i: int):
            if i == len(ss):
                return
            if(ss[i].isalpha()):
                ss[i] = chr(ord(ss[i]) ^ 32)
                r = ''.join(ss)
                self.res.append(r)
                helper(ss, i+1)
                ss[i] = chr(ord(ss[i]) ^ 32)
                helper(ss, i+1)
            else:
                helper(ss, i+1)
        
        self.res.append(S)
        ss = list(S)
        helper(ss, 0)
        return self.res

solution = Solution()


word = "a1B2z"

res = solution.letterCasePermutation(word)
print(res)    

#print(chr(ord('A') ^ 32))    
