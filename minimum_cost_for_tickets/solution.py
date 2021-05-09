from typing import List


class Solution:

    # 983. Minimum Cost For Tickets
    # Difficulty: Medium
    # Time Complexity: O(N) where N equals the number of days
    # explanation
    #   expiring tickets (popping elements from queue) can take at most N time for all days
    #   since the queue can have up to N items
    #   and append / max takes O(1) time
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cost = 0
        last_7day_costs = []
        last_30day_costs = []

        cost_1day_pass, cost_7day_pass, cost_30day_pass = costs

        for day in days:

            # expiring
            while last_7day_costs and last_7day_costs[0][0] + 7 <= day:
                last_7day_costs.pop(0)

            while last_30day_costs and last_30day_costs[0][0] + 30 <= day:
                last_30day_costs.pop(0)

            last_7day_costs.append((day, cost + cost_7day_pass))
            last_30day_costs.append((day, cost + cost_30day_pass))

            # calculate min cost for given day
            # You can either buy 1day pass
            # Or have valid 7day pass
            # Or have valid 30day pass
            cost = min(

                # buying 1day pass
                cost + cost_1day_pass,

                # if your 7day ticket has not expired
                # For example, you bought 7day pass at day 4 and it's day8
                # which means your ticket is still valid
                # so you don't need to pay additional cost for 1day pass
                last_7day_costs[0][1],

                # if your 30day ticket has not expired
                last_30day_costs[0][1]
            )

        return cost

