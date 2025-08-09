class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        edges = defaultdict(list)

        for src, dst in tickets:
            edges[src].append(dst)

        for u, v in edges.items():
            edges[u] = sorted(v, reverse=True)

        path = []

        def dfs(airport):

            while edges[airport]:
                destination = edges[airport].pop()
                dfs(destination)

            path.append(airport)

        dfs("JFK")
        return path[::-1]

