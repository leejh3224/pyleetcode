from typing import List


# 1314. Matrix Block Sum
# Difficulty: Medium
# Time Complexity: O(r * c)
class Solution:

    # reference: https://leetcode.com/problems/matrix-block-sum/discuss/482730/Python-O(-m*n-)-sol.-by-integral-image-technique.-90%2B-with-Explanation
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        mat = [[0] * (n + 1)] + [[0] + row for row in mat]
        answer = [[0] * n for i in range(m)]

        # numbers in the original matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                # computing block sum
                mat[i][j] += mat[i - 1][j] + mat[i][j - 1] - mat[i - 1][j - 1]  # mat[i-1][j-1] is added twice

        for i in range(m):
            for j in range(n):
                r1, r2 = max(0, i - k), min(m, i + k + 1)
                c1, c2 = max(0, j - k), min(n, j + k + 1)

                # D (r2c2) = block sum of whole area
                # B (r2c1) = block sum of upper area
                # C (r1c2) = block sum of left area
                # A (r1c1) = block sum of upper left area
                # block sums share certain areas, so it needs to be considered
                #
                # A --- B
                # |     |
                # C --- D
                #
                # Block sum = D - B - C + A
                # Block sum is also known as summed area table.
                # For more information on summed area table, see https://en.wikipedia.org/wiki/Summed-area_table
                answer[i][j] = mat[r2][c2] - mat[r2][c1] - mat[r1][c2] + mat[r1][c1]

        return answer


