# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.is_number = False
        self.children  = [None for i in range(2)]
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,number):
        cur = self.root
        for i in range(len(number)):
            if not cur.children[int(number[i])]:
                cur.children[int(number[i])] = TrieNode()
            cur = cur.children[int(number[i])]
        cur.is_number = True
    def search(self,number):
        cur = self.root
        ans = ['0'] * 31
        for i in range(len(number)):
            if cur.children[1-int(number[i])]:
                ans[i] = '1'
                cur = cur.children[1-int(number[i])]
            else:
                cur = cur.children[int(number[i])]
        return ans
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        tr = Trie()
        for n in nums:
            a = bin(n)[2:]
            a = (31-len(a))*'0'+a
            tr.insert(a)
        res = 0
        for n in nums:
            a = bin(n)[2:]
            a = (31-len(a))*'0'+ a
            ans = tr.search(a)
            res = max(res,(int(''.join(ans),2)))
        return res