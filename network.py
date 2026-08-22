from collections import defaultdict
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # create a map of ajecency
        # times [[s,d,t],...]
        adjecency = defaultdict(list)
        for source, dest, time in times:
            adjecency[source].append((dest, time))
        # create visited
        visited = [False] * (n + 1)
        # distance map
        distance_to_node = {i: float("inf") for i in range(n + 1)}
        del distance_to_node[0]
        distance_to_node[k] = 0
        # heap que (distance to node, node )
        min_que = [(0, k)]
        while min_que:
            time_to_node, node = heapq.heappop(min_que)
            # check if visited
            if visited[node]:
                continue
            visited[node] = True
            # relaxation
            for neighbour, time_to_neigh in adjecency[node]:
                new_time = time_to_node + time_to_neigh
                if new_time < distance_to_node[neighbour]:
                    distance_to_node[neighbour] = new_time
                    heapq.heappush(min_que, (new_time, neighbour))
        result = max(distance_to_node.values())
        return -1 if result == float("inf") else result


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(Solution().networkDelayTime(times, n, k))
