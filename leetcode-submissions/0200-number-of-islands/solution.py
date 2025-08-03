class UnionFind:
    def __init__(self, grid: List[List[str]]) -> None:
        """
        Initializes a UnionFind data structure
        Initially, each cell with a "1" is its own island.
        """

        self.parent = {}
        self.size = {}
        self.number_of_islands = 0

        m, n = len(grid), len(grid[0])

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    self.number_of_islands += 1

                self.size[(row, col)] = 1
                self.parent[(row, col)] = (row, col)

    def find(self, child: tuple) -> tuple:
        """
        Find with path compression
        """

        if self.parent[child] != child:
            self.parent[child] = self.find(self.parent[child])

        return self.parent[child]

    def union(self, cell1: tuple, cell2: tuple) -> None:
        """
        Union with size
        Decrement the number of islands on each union
        """

        parent1 = self.find(cell1)
        parent2 = self.find(cell2)

        if parent1 == parent2:
            return

        if self.size[parent1] > self.size[parent2]:
            self.parent[parent2] = parent1
            self.size[parent1] += self.size[parent2]
        else:
            self.parent[parent1] = parent2
            self.size[parent2] += self.size[parent1]

        self.number_of_islands -= 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m, n = len(grid), len(grid[0])

        uf = UnionFind(grid)

        movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    for dx, dy in movements:
                        x, y = row + dx, col + dy
                        if 0 <= x < m and 0 <= y < n:
                            if grid[x][y] == "1":
                                uf.union((row, col), (x, y))
                    grid[row][col] = "0"

        return uf.number_of_islands

