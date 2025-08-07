class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # Approach 1: Prim's Algorithm (Eager)
        # O((N ** 2) )

        n = len(points)
        costs = defaultdict(int)
        edges = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):

                p1 = tuple(points[i])
                p2 = tuple(points[j])

                x_val = abs(points[i][0] - points[j][0])
                y_val = abs(points[i][1] - points[j][1])

                manhattan = x_val + y_val
                edges[p1].append(p2)
                edges[p2].append(p1)
                costs[(p1, p2)] = manhattan
                costs[(p2, p1)] = manhattan

        # Choose a source
        source = tuple(points[0])
        n = len(costs)
        m = n - 1

        mst_cost, edges_count = 0, 0
        visited = set()
        min_cost = {tuple(node): float("inf") for node in points}
        parents = {tuple(node): None for node in points}

        heap = []
        heapq.heappush(heap, (0, source))

        # Prim's Algorithm(lazy)
        while heap and edges_count < m:

            cost, node = heapq.heappop(heap)

            # Skip outdated entry
            if cost > min_cost[node]:
                continue

            # Visited node
            if node in visited:
                continue

            visited.add(node)

            if parents[node] is not None:
                mst_cost += cost
                edges_count += 1

            for dest in edges[node]:
                if dest not in visited:
                    edge_cost = costs[(node, dest)]

                    if edge_cost < min_cost[tuple(dest)]:
                        min_cost[dest] = edge_cost
                        parents[dest] = node
                        heapq.heappush(heap, (edge_cost, dest))

        return mst_cost

