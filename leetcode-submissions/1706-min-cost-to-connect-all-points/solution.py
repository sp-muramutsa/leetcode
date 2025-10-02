class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # Prim's

        # Greedily pick cheap edges
        # Use a min heap to get them by min cost

        # MST
            # Undirected graph with min edge cost

        n = len(points)
        edges_count = n - 1
        graph = defaultdict(list)
        costs = {}

        # Make the graph
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    continue
                costs[(i, j)] = abs(points[i-1][0] - points[j-1][0]) + abs(points[i-1][1] - points[j-1][1])
                graph[i].append(j)
                graph[j].append(i)
        
        
        source = 1
        chosen = 0
        visited = set([1])
        min_cost = 0
        heap = []

        for neighbor in graph[source]:
            heapq.heappush(heap, (costs[source, neighbor], neighbor))
        
       
        while heap and chosen < edges_count:
          
            cost, curr = heapq.heappop(heap)

            if curr in visited:
                continue

            visited.add(curr)
            min_cost += cost
            chosen += 1

            for neighbor in graph[curr]:
                if neighbor not in visited:
                    heapq.heappush(heap, (costs[curr, neighbor], neighbor))
        
        return min_cost
             

