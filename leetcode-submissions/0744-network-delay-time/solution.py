class Solution:
    def dijkstra(
        self, source: int, nodes: List[List[int]], cost: Dict[int, int]
    ) -> Dict[int, int]:

        n = len(nodes)
        distances = {node: float("inf") for node in range(1, n + 1)}
        distances[source] = 0

        heap = []
        heapq.heappush(heap, (0, source))
        visited = set()

        while heap:

            du, curr = heapq.heappop(heap)

            if curr in visited:
                continue

            visited.add(curr)

            for neighbor in nodes[curr - 1]:
                new_dist = du + cost[(curr, neighbor)]
                dv = distances[neighbor]

                if new_dist < dv:
                    distances[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

        for x in distances.values():
            if x == float("inf"):
                return -1

        return max(distances.values())

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = [[] for _ in range(n)]
        cost = {}

        for source, destination, time in times:
            adj[source - 1].append(destination)
            cost[(source, destination)] = time

        return self.dijkstra(k, adj, cost)

