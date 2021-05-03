from typing import List


# 547. Number of Provinces
# Difficulty: Medium
# Time Complexity: O(N^2)
class Solution:

    # time complexity is O(N^2) where N = length of isConnected as isConnected is square matrix
    # space complexity is O(N) which is maximum depth of recursion stack
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()

        def dfs(from_city):
            connected_cities = isConnected[from_city]
            visited.add(from_city)

            for to_city in range(n):

                # skip searching when the city is already visited
                # or the city is not reachable
                # or the city is same city where we've left off (no need to search)
                if (to_city in visited) or (connected_cities[to_city] == 0) or (from_city == to_city):
                    continue
                dfs(to_city)

        answer = 0
        for i in range(n):
            if i in visited:
                continue
            dfs(i)

            # exited from recursive dfs
            # which means we've finished searching single province (there's no more city left to reach out)
            answer += 1

        return answer
