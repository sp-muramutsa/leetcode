class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [0 for _ in range(n)]
        self.connected_components = n

    def find(self, x):
        """
        Find with path compression
        """

        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x, y):
        """
        Union with rank heuristic
        """

        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return

        rank_x = self.ranks[parent_x]
        rank_y = self.ranks[parent_y]

        if rank_x > rank_y:
            self.parents[parent_y] = parent_x
        elif rank_x < rank_y:
            self.parents[parent_x] = parent_y
        else:
            self.parents[parent_x] = parent_y
            self.ranks[parent_y] += 1

        self.connected_components -= 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        dsu = DSU(n)
        for src, dest in edges:
            dsu.union(src, dest)

        return dsu.connected_components

