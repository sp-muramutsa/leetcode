class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = [[] for _ in range(n + 1)]
        time = [[0] * (n + 1) for _ in range(n + 1)]

        for u, v, w in times:
            adj[u].append(v)
            time[u][v] = w

        heap = [(0, k)]
        min_t = 0
        min_time = [float("inf") for _ in range(n + 1)]
        min_time[k] = 0

        while heap:

            t, src = heapq.heappop(heap)

            if min_time[src] < t:
                continue

            for dest in adj[src]:
                new_t = t + time[src][dest]
                if new_t < min_time[dest]:
                    min_time[dest] = new_t
                    heapq.heappush(heap, (new_t, dest))

        for x in min_time[1:]:
            if x == float("inf"):
                return -1

        return max(min_time[1:])

