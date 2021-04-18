from typing import List


# 1222. Queens That Can Attack the King
# Difficulty: Medium
# Time Complexity: O(N)
class Solution:

    # Think of the problem in the opposite direction.
    # Instead of check if queen can approach the king, check if the king can approach queens.
    # There are 8 directions the king can move and they are expressed as list of delta.
    # For each direction, the king can move at most 7 steps (8-1).
    # Firstly, as we know the king can't go out of chessboard, we should check that. (out of bounds)
    # Then check if the king encountered a queen along the way.
    # If he does, then add the queen to the answer and break loop (check other directions)
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        size = 8
        deltas = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]

        # Space Complexity: O(1)
        # It's because at most 8 queens can attack the king
        # So the length of an answer is not proportional to the size of the input, queens
        answer = []

        # O(1)
        for delta in deltas:
            dx, dy = delta
            king_x, king_y = king
            can_move = True

            # O(1)
            # king can move at most 7 steps
            for i in range(1, 8):
                x = king_x + (dx * i)
                y = king_y + (dy * i)

                # out of bounds
                if x < 0 or x >= size or y < 0 or y >= size:
                    can_move = False
                    break

                # O(N)
                for queen in queens:
                    queen_x, queen_y = queen

                    # found queen, check other directions
                    if queen_x == x and queen_y == y:
                        answer.append(queen)
                        can_move = False
                        break

                if not can_move:
                    break

            # we are done with this direction
            if not can_move:
                continue

        return answer
