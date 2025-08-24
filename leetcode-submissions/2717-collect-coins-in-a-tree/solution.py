class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:

        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        in_degree = [0 for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            in_degree[u] += 1
            in_degree[v] += 1

        # Phase 1: Remove leaves(or leaf paths) with no coins
        q = deque()
        for node in range(n):
            if in_degree[node] == 1 and coins[node] == 0:
                q.append(node)

        while q:

            curr = q.popleft()
            in_degree[curr] = 0

            for dest in adj[curr]:
                in_degree[dest] -= 1
                if in_degree[dest] == 1 and coins[dest] == 0:
                    q.append(dest)

        # Phase 2: Peel off two layers
        for _ in range(2):
            layer = [node for node in range(n) if in_degree[node] == 1]

            for node in layer:
                in_degree[node] -= 1
                for dest in adj[node]:
                    in_degree[dest] -= 1

        # Count remaining node in the tree
        count = 0
        for a, b in edges:
            if in_degree[a] > 0 and in_degree[b] > 0:
                count += 1

        return 2 * count

