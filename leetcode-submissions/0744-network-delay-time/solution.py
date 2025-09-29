class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)
        weights = {}

        for u, v, w in times:
            graph[u].append(v)
            weights[(u, v)] = w

        distances = {x: float("inf") for x in range(1, n + 1)}
        distances[k] = 0
        heap = [(k, 0)]

        while heap:

            curr, time = heapq.heappop(heap)

            for neighbor in graph[curr]:
                new_time = time + weights[(curr, neighbor)]

                if new_time < distances[neighbor]:
                    distances[neighbor] = new_time
                    heapq.heappush(heap, (neighbor, new_time))

        answer = max(distances.values())
        return answer if answer != float("inf") else -1

