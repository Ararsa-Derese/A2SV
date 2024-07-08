# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class WeightedUnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.group = [set([i]) for i in range(n)]
    
    def _root(self, node: int) -> int:
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    
    def find(self, node1: int, node2: int) -> bool:
        return self._root(node1) == self._root(node2)
    
    def union(self, node1: int, node2: int) -> None:
        root1, root2 = self._root(node1), self._root(node2)
        if len(self.group[root1]) < len(self.group[root2]):
            root1, root2 = root2, root1
        self.parent[root2] = root1
        self.group[root1] |= self.group[root2]

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = WeightedUnionFind((l := len(s)))
        for a, b in pairs:
            uf.union(a, b)
        res = ['']*l
        for root in [i for i, node in enumerate(uf.parent) if node == i]:
            for i, ch in zip(sorted(uf.group[root]), sorted(s[i] for i in uf.group[root])):
                res[i] = ch
        return ''.join(res)