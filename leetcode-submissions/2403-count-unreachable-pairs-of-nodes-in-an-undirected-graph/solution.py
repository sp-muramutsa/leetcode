class UnionFind:
    def __init__(self, n):
        self.parents = {i: i for i in range(n)}
        self.sizes = {i: 1 for i in range(n)}

    def find(self, child):
        if self.parents[child] != child:
            self.parents[child] = self.find(self.parents[child])
        return self.parents[child]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return

        size_x = self.sizes[parent_x]
        size_y = self.sizes[parent_y]

        if size_x > size_y:
            self.parents[parent_y] = parent_x
            self.sizes[parent_x] += size_y
        else:
            self.parents[parent_x] = parent_y
            self.sizes[parent_y] += size_x


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        uf = UnionFind(n)

        for src, dest in edges:
            uf.union(src, dest)

        total_unreachable = 0
        for node in range(n):
            total_unreachable += n - uf.sizes[uf.find(node)]

        return total_unreachable // 2

