from typing import List


# 841. Keys and Rooms
# Difficulty: Medium
# Time Complexity: O(N + E) where N = length of room and E = length of keys in each room
class Solution:

    # Typical dfs problem
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        opened = set()
        
        def dfs(i):
            if i in opened:
                return

            opened.add(i)
            for j in rooms[i]:
                dfs(j)
  
        dfs(0)

        return len(opened) == len(rooms)
