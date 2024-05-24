# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = [None for _ in range(26)]
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        cur = self.root
        for s in word:
            if not cur.children[ord(s)-97]:
                cur.children[ord(s)-97] = TrieNode()
            cur = cur.children[ord(s)-97]
        cur.is_word = True
    def check(self,word):
        cur = self.root
        for s in word:
            if not cur.children[ord(s)-97]:
                return False
            if not cur.children[ord(s)-97].is_word:
                return False
            cur = cur.children[ord(s)-97]
        return True
class Solution:
    def longestWord(self, words: List[str]) -> str:
        tr = Trie()
        words.sort()
        for word in words:
            tr.insert(word)
        ans = ""
        for word in words:
            if tr.check(word):
                if len(ans)<len(word):
                    ans = word
        return ans