class UnionFind:
    def __init__(self, adj):
        self.parents = {}
        self.ranks = {}

        for u, v in adj:
            self.parents[u] = u
            self.parents[v] = v
            self.ranks[u] = 1
            self.ranks[v] = 1

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):

        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return

        if self.ranks[parent_x] > self.ranks[parent_y]:
            self.parents[parent_y] = parent_x
        elif self.ranks[parent_x] < self.ranks[parent_y]:
            self.parents[parent_x] = parent_y
        else:
            self.parents[parent_y] = parent_x
            self.ranks[parent_x] += 1


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        uf = UnionFind(edges)

        for u, v in edges:
            parent_u = uf.find(u)
            parent_v = uf.find(v)

            if parent_u == parent_v:
                return False

            uf.union(u, v)

        return True

