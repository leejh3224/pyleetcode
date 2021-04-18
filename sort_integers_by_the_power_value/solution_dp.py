# 1387. Sort Integers by The Power Value
# Difficulty: Medium
# Time Complexity: unknown
class Solution:

    # Solution using memoization
    def getKth(self, lo, hi, k):

        # get_power of 1 equals 0
        memo = {1: 0}

        def get_power(n):

            # answer found in hashmap
            if n in memo:
                return memo[n]
            else:
                if n % 2 == 1:

                    # we're going one step further, so add 1
                    memo[n] = 1 + get_power(3 * n + 1)
                else:
                    memo[n] = 1 + get_power(n >> 1)

            return memo[n]

        values_with_power = [(get_power(x), x) for x in range(lo, hi + 1)]

        # tuples are sorted by first element by default
        return sorted(values_with_power)[k - 1][1]

