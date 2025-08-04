class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        adj = [[] for _ in range(n)]
        artificial = [[] for _ in range(n)]

        for src, dest in connections:
            adj[dest].append(src)
            artificial[dest].append(src)
            artificial[src].append(dest)

        visited = set()
        visited.add(0)
        reorder = 0
        q = deque([0])

        while q:

            curr = q.popleft()

            for child in artificial[curr]:
                if child not in visited:
                    # There is an edge from child to parent
                    if curr in adj[child]:
                        reorder += 1
                    visited.add(child)
                    q.append(child)

        return reorder

