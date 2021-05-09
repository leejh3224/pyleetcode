import sys

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
num_tc = int(input())

# 놀이공원
# Difficulty: 3
# Time Complexity: O(N^2) where N is the size of the matrix
# related
#  - https://www.techiedelight.com/find-maximum-sum-submatrix-in-given-matrix/
#  - https://leetcode.com/problems/matrix-block-sum/
for _ in range(num_tc):
    N, K = [int(n) for n in input().split(" ")]
    grid = [[int(n) for n in input().split(" ")] for _ in range(N)]

    grid = [[0] * (N + 1)] + [[0] + row for row in grid]

    # summed area table
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            grid[i][j] += grid[i - 1][j] + grid[i][j - 1] - grid[i - 1][j - 1]

    submatrix_sum = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    # k * k submatrix sum
    for i in range(K, N + 1):
        for j in range(K, N + 1):
            submatrix_sum[i][j] += grid[i][j] - grid[i - K][j] - grid[i][j - K] + grid[i - K][j - K]

    answer = sys.maxsize

    for i in range(K, N + 1):
        for j in range(K, N + 1):
            answer = min(answer, submatrix_sum[i][j])

    print(answer)
