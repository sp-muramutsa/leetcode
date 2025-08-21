class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        adj = [[] for _ in range(n)]
        visited = set()

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(parent):

            visited.add(parent)
            parent_time = 0

            for child in adj[parent]:

                if child in visited:
                    continue

                child_time = dfs(child)
                if child_time > 0 or hasApple[child]:
                    parent_time += 2 + child_time

            return parent_time

        return dfs(0)

