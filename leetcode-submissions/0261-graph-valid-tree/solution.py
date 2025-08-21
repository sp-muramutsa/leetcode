class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # We are going to check the parent of the node between edged nodes
        # Create a rank to show number of children
        # Implement the find function
        # Implement the union function
        # Parents are the same return False
        # Return True
        # Iterate over the eges and operate union find
        # If union is False return False
        # Return True at the end of the for loop
        if len(edges) != n-1:
            return False

        parent = [i for i in range(n)]
        rank = [1] * n

        def find(n):
            if parent[n] != n:
                parent[n] = find(parent[n])

            return parent[n]

        def union(edge):
            p1 = find(edge[0])
            p2 = find(edge[1])

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]

            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True

        for edge in edges:
            if not union(edge):
                return False

        return True

