class Solution:
    def in_bound(self, i, j, n , m):
        return 0 <= i < n and 0 <= j < m
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
      

        def rec(i,j,idx):
            if idx == len(word):
                return True
            for rc,rl in directions:
                ni  = i + rc
                nj = j + rl
                if self.in_bound(ni, nj, len(board),len(board[0])):
                    if board[ni][nj] == word[idx]:
                        if (ni , nj) not in a:
                            a.add((ni,nj))
                            if rec(ni , nj, idx+1):
                                return True
                            a.remove((ni,nj))
        a=set()
        idx=0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[idx]:
                    a.add((i,j))
                    if rec(i,j,idx+1):
                        return True
                    a.remove((i,j))

        return False

