# 1400. Construct K Palindrome Strings
# Difficulty: Medium
# Time Complexity: O(N)
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        # length of smallest possible palindrome is 1
        # so if k exceeds length of s, it's not possible to construct k palindromes
        if len(s) < k:
            return False

        counts = {}
        for ch in s:
            counts[ch] = 1 + counts.get(ch, 0)

        values = list(counts.values())
        num_odd_keys = 0

        # it can be expressed with list comprehension
        # sum(freq[c]&1 for c in freq)
        for count in values:
            if count % 2 != 0:
                num_odd_keys += 1

        # chars with odd number of frequencies can construct palindrome by itself
        # so it exceeds k then it's impossible to construct only k palindromes
        return num_odd_keys <= k
