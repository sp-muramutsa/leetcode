class UnionFind:
    def __init__(self, grid: List[List[int]], nodes: List[tuple]) -> None:
        self.parents = {}
        self.sizes = {}
        self.grid = grid

        for node in nodes:
            print(node)
            self.parents[node] = node

            r, c = node
            if self.grid[r][c] == 1:
                self.sizes[node] = 1
            else:
                self.sizes[node] = 0

    def find(self, child: tuple) -> tuple:
        """
        Find with path compression
        """

        parent = self.parents[child]
        if parent != child:
            self.parents[child] = self.find(parent)

        return self.parents[child]

    def union(self, node1: tuple, node2: tuple) -> None:
        """
        Union with size heuristic
        """

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
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        cells = [(row, col) for row in range(m) for col in range(n)]
        uf = UnionFind(grid, cells)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    for dx, dy in directions:
                        x, y = row + dx, col + dy
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                            uf.union((row, col), (x, y))

        return max(uf.sizes.values())

