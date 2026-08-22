from itertools import islice
from typing import List
from collections import defaultdict
from collections import deque

from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1. Build the adjacency list
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # 2. Track the minimum time to reach each node (1-indexed)
        # Initialize everything to infinity
        min_times = {i: float("inf") for i in range(1, n + 1)}
        min_times[k] = 0

        # 3. Min-heap stores tuples of (accumulated_time, current_node)
        # We start at node k with 0 time
        min_heap = [(0, k)]
        visited = set()

        while min_heap:
            current_time, node = heapq.heappop(min_heap)

            # If we've already processed this node's shortest path, skip it
            if node in visited:
                continue
            visited.add(node)

            # Explore neighbors
            for neighbor, weight in graph[node]:
                new_time = current_time + weight
                # If we found a faster way to the neighbor, update and push to heap
                if new_time < min_times[neighbor]:
                    min_times[neighbor] = new_time
                    heapq.heappush(min_heap, (new_time, neighbor))

        # 4. Check results
        # If we couldn't visit all n nodes, return -1
        if len(visited) < n:
            return -1

        # Otherwise, the total delay time is the maximum of the shortest paths
        return max(min_times.values())


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
times = [[1, 2, 1]]
times = [[1, 2, 1], [2, 1, 3]]
n = 4
n = 2
k = 2
print(Solution().networkDelayTime(times, n, k))
