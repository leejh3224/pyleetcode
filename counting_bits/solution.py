from typing import List


# 1472. Design Browser History
# Difficulty: Medium
# Time Complexity: O(N)
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)

        # Least Significant Bit (LSB) is always 0 for even numbers and 1 for odd numbers
        # It means if we right shift any even numbers by 1, chances are the count of 1 will still remain the same
        # However if we do the same for any odd numbers, it would lose LSB of 1 (it needs to be compensated)
        # For example,
        # # of 1 is same for 10(2) and 100(4) or 11(3) and 110(6)
        # This holds for odd numbers as well. (1(1) and 11(3) or 101(5) and 10(2))
        for n in range(num + 1):

            # n >> 1: number at n // 2
            # n & 1: compensate 1 for odd numbers
            dp[n] = dp[n >> 1] + (n & 1)
        return dp
