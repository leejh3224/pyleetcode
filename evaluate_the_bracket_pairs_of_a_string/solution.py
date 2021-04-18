from typing import List


# 1807. Evaluate the Bracket Pairs of a String
# Difficulty: Medium
# Time Complexity: O(N^2)
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        k = dict((k, v) for k, v in knowledge)
        stack = []

        # O(N)
        for ch in s:
            if ch != ')':
                stack.append(ch)

            # We've encountered ) so the stack should look like
            # ['other', 'characters', '(', 'k', 'e', 'y']
            else:
                word = []

                # O(N)
                # # of operations are sum of len(key)
                # and in worst case, sum of len(key) is O(N)
                # so the algorithm has O(N^2) time complexity
                while stack[-1] != '(':
                    word.append(stack.pop())

                # remove remaining (
                stack.pop()
                stack.append(k.get(''.join(word[::-1]), '?'))

        return ''.join(stack)

