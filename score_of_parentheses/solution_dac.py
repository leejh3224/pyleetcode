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

            # Divide and Conquer Solution
            # Given (()(()))
            # 1: 2 * '()(())'
            # 2: 2 * (1 + 2 * '()')
            # 3: 2 * (1 + 2) = 6
            for i in range(start, end):
                balance += 1 if S[i] == '(' else -1

                if balance != 0:
                    continue

                # substring is balanced and forms ()
                if i == start + 1:
                    answer += 1
                else:

                    # substring is balanced but is outer parentheses
                    answer += 2 * dac(start + 1, i)

                # move head one step forward
                # think of case ()()
                # without start = i + 1, it returns 3
                start = i + 1

            return answer

        return dac(0, len(S))
