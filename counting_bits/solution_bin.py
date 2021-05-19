from typing import List


# 1472. Design Browser History
# Difficulty: Medium
# Time Complexity: -
class Solution:
    def countBits(self, num: int) -> List[int]:
        def dec_to_bin(x):
            return bin(x)[2:]
        return [dec_to_bin(n).count("1") for n in range(num + 1)]
