from typing import List


# 529. Minesweeper
# Difficulty: Medium
# Time Complexity: O(m*n) where m*n equals the number of elements in board
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        x, y = click

        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            queue = [(x, y)]

            while queue:
                i, j = queue.pop(0)

                if board[i][j] != 'E':
                    continue

                adjs = [(x, y) for x, y in (
                (i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j),
                (i + 1, j + 1)) if 0 <= x < m and 0 <= y < n]
                mines = sum(board[x][y] == 'M' for x, y in adjs)

                if not mines:
                    board[i][j] = 'B'
                    for x, y in adjs:
                        queue.append((x, y))
                else:
                    board[i][j] = str(mines)

        return board
