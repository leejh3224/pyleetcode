from typing import List


# 1314. Matrix Block Sum
# Difficulty: Medium
# Time Complexity: O(r^2 * c^2)
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        answer = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                _sum = 0

                r1 = max(0, i - k)
                r2 = min(i + k, m - 1)
                c1 = max(0, j - k)
                c2 = min(j + k, n - 1)

                for r in range(r1, r2 + 1):
                    _sum += sum(mat[r][c1:c2 + 1])

                answer[i][j] = _sum

        return answer
