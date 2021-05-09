from typing import List


class Solution:

    # 959. Regions Cut By Slashes
    # Difficulty: Medium
    # Time Complexity: O(N*M) where N*M refers to # of elements in grid
    # explanation:
    #   drawing slash on up-scaled grid takes O(N*M) time
    #   and solving the number of islands problem also takes O(N*M) time
    #   so it takes at most O(N*M) time
    def regionsBySlashes(self, grid: List[str]) -> int:
        n, m = len(grid), len(grid[0])

        # up-scaled grid
        u_grid = [[0 for _ in range(3 * m)] for _ in range(3 * n)]

        # draw slash on up-scaled grid
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "/":
                    u_grid[i * 3][j * 3 + 2] = u_grid[i * 3 + 1][j * 3 + 1] = u_grid[i * 3 + 2][j * 3] = 1
                if grid[i][j] == "\\":
                    u_grid[i * 3][j * 3] = u_grid[i * 3 + 1][j * 3 + 1] = u_grid[i * 3 + 2][j * 3 + 2] = 1

        def dfs(i, j):
            within_bounds = 0 <= i < n * 3 and 0 <= j < m * 3

            if within_bounds and u_grid[i][j] == 0:

                # mark as visited
                u_grid[i][j] = 1

                # visit all four directions
                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)

        answer = 0

        # solving number of islands problem
        for i in range(n * 3):
            for j in range(m * 3):
                if u_grid[i][j] == 0:
                    dfs(i, j)

                    # the moment you exit the call stack, you've explored one island
                    answer += 1

        return answer
