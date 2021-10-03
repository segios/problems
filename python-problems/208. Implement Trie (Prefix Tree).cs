/*
# https://leetcode.com/problems/implement-trie-prefix-tree/
# 208. Implement Trie (Prefix Tree)
# Medium
# Design, Trie
#  
*/
using System.Collections.Generic;

public class TrieNode {
    public TrieNode (){
    }
    public TrieNode (char value , bool isTerminated ){
        Value = value;
        IsTerminated = isTerminated;
    }
    public bool IsTerminated { get; set; }
    public char Value { get; set; }
    private Dictionary<char, TrieNode> childNodes = new Dictionary<char, TrieNode>();

    public TrieNode Find(char v){
        return childNodes.ContainsKey(v) ?
            childNodes[v] : null;
    }

    public TrieNode AddChild(TrieNode node){
        if(!childNodes.ContainsKey(node.Value)){
            childNodes[node.Value] = node;
        }
        childNodes[node.Value].IsTerminated = childNodes[node.Value].IsTerminated  || node.IsTerminated;
        return childNodes[node.Value] ;
    }

    public TrieNode AddChild(char v, bool isTerminated){
        if(!childNodes.ContainsKey(v)){
            childNodes[v] = new TrieNode(v, isTerminated);
        }
        childNodes[v].IsTerminated = childNodes[v].IsTerminated  || isTerminated;
        return childNodes[v] ;
    }
}
public class Trie {

    TrieNode root;
    /** Initialize your data structure here. */
    public Trie() {
        root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    public void Insert(string word) {
        var current = root;
        var last = word.Length - 1;
        for(var i=0;i < word.Length;i++){
            var l = word[i];
            current = current.AddChild(l, i == last);
        }
    }
    
    /** Returns if the word is in the trie. */
    public bool Search(string word) {
        var current = Find(word);
        return current?.IsTerminated ?? false;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public bool StartsWith(string prefix) {
        
        return Find(prefix) != null;
    }

     private TrieNode Find(string prefix) {
        var current = root;
        var last = prefix.Length - 1;
        for(var i=0;i < prefix.Length;i++){
            var l = prefix[i];
            current = current.Find(l);
            if (current == null)
                return null;
        }
        return current;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.Insert(word);
 * bool param_2 = obj.Search(word);
 * bool param_3 = obj.StartsWith(prefix);
 */