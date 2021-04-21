from typing import List


# 529. Minesweeper
# Difficulty: Medium
# Time Complexity: O(m*n) where m*n equals the number of elements in board
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i, j, m, n = *click, len(board), len(board[0])

        def dfs(i, j):
            if board[i][j] != 'E':
                return

            adjs = [(x,y) for x,y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)) if 0 <= x < m and 0 <= y < n]
            mines = sum(board[x][y] == 'M' for x,y in adjs)

            if not mines:
                board[i][j] = 'B'
                for x,y in adjs:
                    dfs(x,y)
            else:
                board[i][j] = str(mines)

        if board[i][j] == 'M':
            board[i][j] = 'X'
        else:
            dfs(i,j)

        return board
