from typing import List


# 1701. Average Waiting Time
# Difficulty: Medium
# Time Complexity: O(N)
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        now = 0
        waiting_times = []

        for customer in customers:
            arrival, time = customer
            now = max(now, arrival) + time
            waiting_times.append(now - arrival)

        return sum(waiting_times) / len(customers)
