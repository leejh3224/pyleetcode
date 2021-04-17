# 856. Score of Parentheses
# Difficulty: Medium
# Time Complexity: O(N^2)
class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        def dac(start, end):
            answer = balance = 0

            for i in range(start, end):
                balance += 1 if S[i] == '(' else -1

                if balance != 0:
                    continue

                if i == start + 1:
                    answer += 1
                else:
                    answer += 2 * dac(start + 1, i)
                start = i + 1

            return answer

        return dac(0, len(S))
