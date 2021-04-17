# 856. Score of Parentheses
# Difficulty: Medium
# Time Complexity: O(N)
class Solution(object):
    def scoreOfParentheses(self, S):
        stack = [0]

        for s in S:
            if s == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)

        return stack.pop()
