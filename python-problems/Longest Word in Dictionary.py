# https://leetcode.com/problems/longest-word-in-dictionary/
# 720. Longest Word in Dictionary
# Easy
# Trie, Hash Table
#  A/D (Trie)

from typing import List
from collections import deque
import itertools 


class Solution:
    def longestWord(self, words: List[str]) -> str:
        wordHash = {}

        for w in words:
            wordHash[w] = 1

        res = None

        for w in words:
            word = ''
            for li in range(0, len(w)): 
                if(li == len(w)-1):
                    if not res:
                        res = w
                    elif len(w) > len(res):
                        res = w
                    elif len(w) == len(res):
                        res = w if w < res else res
                else:
                    word = word + w[li]
                    if word not in wordHash:
                        break; 
        return res

solution = Solution()

res = solution.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"])
print (res)


class Solution1(object):
    def longestWord(self, words):
        ans = ""
        wordset = set(words)
        for word in words:
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                if all(word[:k] in wordset for k in range(1, len(word))):
                    ans = word

        return ans

class Solution2(object):
    def longestWord(self, words):
        wordset = set(words)
        words.sort(key = lambda c: (-len(c), c))
        for word in words:
            if all(word[:k] in wordset for k in range(1, len(word))):
                return word

        return ""    


# trie
class SolutionTrie(object):
    def longestWord(self, words):
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)[END] = i
            #reduce(func, iterable, initializer=None),

        stack = trie.values()
        ans = ""
        while stack:
            cur = stack.pop()
            if END in cur:
                word = words[cur[END]]
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                stack.extend([cur[letter] for letter in cur if letter != END])

        return ans