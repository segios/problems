from typing import List

class TrieNode:
    def __init_(self, c: str, end: bool):
        self.c = c
        self.nodes : List[TrieNode] = [None] * 26
        self.end = end


class Trie:
    def __init_(self, products: List[str]):
        self.nodes : List[TrieNode] = [None] * 26
        
        for p in products:
            self.addWord(p)

    def addWord(self, word: str):
        nodes = self.nodes

        for i in range(len(word)):
            l = word[i]
            if not nodes[int(l)]:
                nodes[int(l)] = TrieNode(l, i == len(word) - 1)
            nodes = nodes[int(l)].nodes

        

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        