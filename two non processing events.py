import heapq
from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        pq = []  # min-heap of (endTime, value)

        best_single = 0
        ans = 0

        for start, end, value in events:
            while pq and pq[0][0] < start:
                best_single = max(best_single, pq[0][1])
                heapq.heappop(pq)

            ans = max(ans, best_single + value)
            ans = max(ans, value)

            heapq.heappush(pq, (end, value))

        return ans
