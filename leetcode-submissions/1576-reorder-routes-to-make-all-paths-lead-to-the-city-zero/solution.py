class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        reorder = 0

        adj = defaultdict(list)
        alt = defaultdict(list)

        for u, v in connections:
            adj[u].append(v)
            alt[u].append(v)
            alt[v].append(u)

        visited = set()
        print(alt)
        print(adj)

        def dfs(node):

            visited.add(node)

            for neighbor in alt[node]:
                if neighbor in visited:
                    continue

                if neighbor in adj[node]:
                    nonlocal reorder
                    reorder += 1

                dfs(neighbor)

        dfs(0)
        return reorder

