from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sum = [sum(piles[i:]) for i in range(n)]

        @lru_cache(None)
        def game(i, m):
            if i + 2 * m >= len(piles):
                return suffix_sum[i]
            
            min_score = 2 ** 31 - 1
            
            for x in range(1, 2 * m + 1):
                next_start = i + x
                next_m = max(x, m)

                score = game(next_start, next_m)
                min_score = min(score, min_score)

            return suffix_sum[i] - min_score
        
        return game(0, 1)
