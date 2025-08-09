class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # Bellman Ford's

        edges = [[] * n for _ in range(n)]
        prices = [[0] * n for _ in range(n)]

        for fro, to, price in flights:
            edges[fro].append(to)
            prices[fro][to] = price

        cheapest = [float("inf")] * n
        cheapest[src] = 0

        for _ in range(k + 1):
            temp_cheapest = cheapest.copy()
            for u in range(n):
                for v in edges[u]:
                    new_price = temp_cheapest[u] + prices[u][v]
                    if new_price < cheapest[v]:
                        cheapest[v] = new_price

        cheapest_flight = cheapest[dst]
        return cheapest_flight if cheapest_flight != float("inf") else -1

