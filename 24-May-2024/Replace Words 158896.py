# Problem: Replace Words - https://leetcode.com/problems/replace-words/

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
    def search(self,word):
        cur = self.root
        ans = ""
        for s in word:
            if not cur.children[ord(s)-97]:
                break
            ans+=s
            if cur.children[ord(s)-97].is_word:
                return ans
            cur = cur.children[ord(s)-97]
            
        if cur.is_word:
            return ans
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        tr = Trie()
        for word in dictionary:
            tr.insert(word)
        st =sentence.split()
        for i in range(len(st)):
            st[i] = tr.search(st[i])
        return ' '.join(st)
