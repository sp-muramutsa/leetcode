class DSU:
    def __init__(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        self.parents = {}
        self.sizes = {}
        self.num_islands = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    self.parents[(row, col)] = (row, col)
                    self.sizes[(row, col)] = 1
                    self.num_islands += 1

    def find(self, x):

        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x, y):

        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return

        if self.sizes[parent_x] > self.sizes[parent_y]:
            self.parents[parent_y] = parent_x
            self.sizes[parent_x] += self.sizes[parent_y]
        else:
            self.parents[parent_x] = parent_y
            self.sizes[parent_y] = self.sizes[parent_x]

        self.num_islands -= 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        dsu = DSU(grid)
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    for dx, dy in directions:
                        nr, nc = row + dx, col + dy
                        if not (0 <= nr < ROWS and 0 <= nc < COLS):
                            continue
                        if grid[nr][nc] == "1":
                            dsu.union((row, col), (nr, nc))

        return dsu.num_islands

