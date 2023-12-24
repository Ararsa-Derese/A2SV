class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dic = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                b = (i//3,j//3)
                if board[i][j] in dic[i] or board[i][j] in dic[j+9] or board[i][j] in dic[b]:
                    return False
                else:
                    dic[i].add(board[i][j])
                    dic[j+9].add(board[i][j])
                    dic[b].add(board[i][j])
        return True