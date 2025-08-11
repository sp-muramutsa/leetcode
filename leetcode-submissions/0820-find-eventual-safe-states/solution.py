class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        n = len(graph)
        in_degree = [0] * n
        q = deque()
        adj = [[] for _ in range(n)]

        for src in range(n):
            for dest in graph[src]:
                adj[dest].append(src)

        in_degree = [len(graph[node]) for node in range(n)]
        q = deque([node for node in range(n) if in_degree[node] == 0])
        safe = [False] * n

        while q:

            curr = q.popleft()
            safe[curr] = True

            for dst in adj[curr]:
                in_degree[dst] -= 1
                if in_degree[dst] == 0:
                    q.append(dst)

        return [node for node in range(n) if safe[node]]

