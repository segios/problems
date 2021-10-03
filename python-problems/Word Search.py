# https://leetcode.com/problems/word-search/
# 79. Word Search
# Medium
# Arrays, Backtracking
# A
# 

from typing import List
from collections import Counter

class Solution:
    def exist(self, board, word):
        def preCheck():
            preDict = {}
            for i in word:
                if i in preDict: preDict[i]+=1
                else: preDict[i] = 1
            for i in board:
                for j in i:
                    if j in preDict and preDict[j]>0: preDict[j]-=1
            for i in preDict.values():
                if i>0: return False
            return True
        def helper(wordIdx, x, y):
            if board[x][y] != word[wordIdx]: return False
            elif wordIdx == l-1: return True
            else:
                wordIdx += 1
                tempChar = board[x][y]
                board[x][y] = None
                for d in [(0,1),(0,-1),(1,0),(-1,0)]:
                    xNext = x+d[0]
                    yNext = y+d[1]
                    if -1<xNext<m and -1<yNext<n and board[xNext][yNext]: 
                        if helper(wordIdx, xNext, yNext): return True
                board[x][y] = tempChar
                return False
        if not board: return False
        if not word: return True
        if not preCheck(): return False
        m = len(board)
        n = len(board[0])
        l = len(word)
        for i in range(m):
            for j in range(n):
                if helper(0,i,j): return True
        return False

    def exist1(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        if not word:
            return False
#        if len(word) > 15:
#            return False
        leny, lenx = len(board), len(board[0])
 #       if leny < 0 or leny > 6 or lenx < 0 or lenx > 6 :
 #           return False

        self.usedLetters = set()

        for i in range(leny):
            for j in range(lenx):
                if board[i][j] == word[0]:
                    if self.check(i, j, 0, board, word):
                        return True
        return False

    def check(self, i, j, charIdx, board: List[List[str]], word: str) -> bool:
        letter = word[charIdx]

        rec = str(i) +'_' +  str(j) + '_' + letter
        if rec in self.usedLetters:
            return False

        self.usedLetters.add(rec)

        if charIdx == len(word) - 1 :
            return True

        leny, lenx = len(board), len(board[0])
        charIdx += 1;
        
        if charIdx >= len(word):
            return False

        letter = word[charIdx]

        if i-1 >= 0 and board[i-1][j] == letter:
            if self.check(i-1, j, charIdx, board, word):
                return True

        if i >= 0 and j-1 >= 0 and board[i][j-1] == letter:
            if self.check(i, j-1, charIdx, board, word):
                return True

        if i >= 0 and j+1 < lenx and board[i][j+1] == letter:
            if self.check(i, j+1, charIdx, board, word):
                return True

            
        if i+1 < leny and board[i+1][j] == letter:
            if self.check(i+1, j, charIdx, board, word):
                return True

        self.usedLetters.remove(rec)
        return False

solution = Solution()



m = [["b","a","a","b","a","b"],
     ["a","b","a","a","a","a"],
     ["a","b","a","a","a","b"],
     ["a","b","a","b","b","a"],
     ["a","a","b","b","a","b"],
     ["a","a","b","b","b","a"],
     ["a","a","b","a","a","b"]]
word = "aabbbbabbaababaaaabababbaaba"
#m = [[1,2],[3,4]]
res = solution.exist(m, word)
print(res)    