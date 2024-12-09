class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        hashmap = {}
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        def dfs(r, c):
            if (r<0 or c<0 or r==ROWS or c==COLS) or board[r][c]!="O" or hashmap.get(tuple([r,c])) ==1:
                return
            hashmap[tuple([r,c])] = 1
            for dr,dc in directions:
                dfs(r+dr,c+dc)
        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r,0)
            if board[r][COLS-1] == "O":
                dfs(r,COLS-1)
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)
            if board[ROWS-1][c] == "O":
                dfs(ROWS-1,c)
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in hashmap.keys():
                    board[r][c] = "X"
