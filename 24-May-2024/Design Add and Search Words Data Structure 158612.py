# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        cur = self.root
        for s in word:
            if s not in cur.children:
                cur.children[s] = TrieNode()
            cur = cur.children[s]
        cur.is_end = True

    def search(self, word: str) -> bool:
        def rec(curr,i):
            if i==len(word):
                return curr.is_end
            
            if word[i]=='.':
                for child in curr.children.values():
                    if rec(child,i+1):
                        return True
                return False

            if word[i] not in curr.children:
                return False
                
            return rec(curr.children[word[i]],i+1)
  

        return rec(self.root,0)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)