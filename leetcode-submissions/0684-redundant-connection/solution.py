class UnionFind:
    def __init__(self, n: int):
        self.parents = {i: i for i in range(1, n + 1)}
        self.sizes = {j: 1 for j in range(1, n + 1)}

    def find(self, node: int) -> int:
        """
        Find with path compression
        """

        parent = self.parents[node]
        if parent != node:
            self.parents[node] = self.find(parent)

        return self.parents[node]

    def union(self, node1: int, node2: int) -> Optional[List[int]]:
        """
        Union with size heuristic
        """

        parent1 = self.find(node1)
        parent2 = self.find(node2)

        # Connected component
        if parent1 == parent2:
            return [node1, node2]

        # Otherwise, the component is unconnected. Just union.
        if self.sizes[parent1] > self.sizes[parent2]:
            self.parents[parent2] = parent1
            self.sizes[parent1] += self.sizes[parent2]
        else:
            self.parents[parent1] = parent2
            self.sizes[parent2] += self.sizes[parent1]


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        uf = UnionFind(n)
        redundant_connection = []

        for src, dest in edges:
            temp = uf.union(src, dest)
            if temp:
                redundant_connection = temp

        return redundant_connection

