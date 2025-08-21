class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Get the number of nodes
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1] * (n+1)

        # Find
        def find(n):
            if parent[n] == n:
                return n

            return find(parent[n])

        # Union
        def union(n1, n2):
            e1 = find(n1)
            e2 = find(n2)

            if e1 == e2:
                return False

            rank[e2] += 1
            if rank[e1] > rank[e2]:
                parent[e2] = e1
                rank[e1] += rank[e2]

            else:
                parent[e1] = e2
                rank[e2] += rank[e1]

            return True

        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge
