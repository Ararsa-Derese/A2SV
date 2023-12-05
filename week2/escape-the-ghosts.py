class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        for g in ghosts:
            if (abs(g[0]-target[0])+abs(g[1]-target[1]))<= abs(target[0])+abs(target[1]):
                return False
        return True