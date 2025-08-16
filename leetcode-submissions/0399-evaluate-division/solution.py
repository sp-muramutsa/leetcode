class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        weights = {}
        adj = defaultdict(set)

        for i, (A, B) in enumerate(equations):
            weights[(A, B)] = values[i]
            weights[(B, A)] = 1 / values[i]
            adj[A].add(B)
            adj[B].add(A)

        def bfs(source, goal):

            q = deque([(1.0, source)])
            visited = set([source])

            while q:

                curr_weight, curr = q.popleft()

                if curr == goal:
                    return curr_weight

                for dest in adj[curr]:
                    if dest in visited:
                        continue

                    visited.add(dest)

                    q.append((curr_weight * weights[(curr, dest)], dest))

            return -1.0

        result = []
        for C, D in queries:
            if C not in adj or D not in adj:
                result.append(-1.0)
            elif C == D:
                result.append(1.0)
            else:
                weight = bfs(C, D)
                result.append(weight)

        return result

