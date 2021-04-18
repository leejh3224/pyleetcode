# 1387. Sort Integers by The Power Value
# Difficulty: Medium
# Time Complexity: unknown
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        # Brute force
        # compute power of every numbers in range
        v = sorted(list(range(lo, hi + 1)), key=lambda e: self.get_power(e))
        return v[k - 1]

    # Collatz conjecture
    # Time complexity of it is unknown
    # reference: https://cs.stackexchange.com/questions/54266/how-long-does-the-collatz-recursion-run
    def get_power(self, x):
        power = 0

        while x != 1:
            power += 1
            if x % 2 == 0:
                x /= 2
            else:
                x = 3 * x + 1

        return power
