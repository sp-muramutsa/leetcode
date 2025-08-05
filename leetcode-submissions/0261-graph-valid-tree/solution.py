class DSU:
    def __init__(self, n):
        self.parents = {i: i for i in range(n)}
        self.sizes = {i: 1 for i in range(n)}

    def find(self, node):

        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])

        return self.parents[node]

    def union(self, node1, node2):

        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 == parent2:
            return

        if self.sizes[parent1] > self.sizes[parent2]:
            self.parents[parent2] = parent1
            self.sizes[parent1] += self.sizes[parent2]
        else:
            self.parents[parent1] = parent2
            self.sizes[parent2] += self.sizes[parent1]


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
   
        dsu = DSU(n)
        for src, dest in edges:
            parent1 = dsu.find(src)
            parent2 = dsu.find(dest)

            if parent1 == parent2:
                return False
            dsu.union(src, dest)

        return len(edges) == n - 1

