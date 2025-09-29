class UnionFind:
    def __init__(self, grid):
        self.parents = {}
        self.sizes = {}

        ROWS, COLS = len(grid), len(grid[0])

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    self.parents[(row, col)] = (row, col)
                    self.sizes[(row, col)] = 1

    def collapsing_find(self, x):

        if self.parents[x] != x:
            self.parents[x] = self.collapsing_find(self.parents[x])
        return self.parents[x]

    def weighted_union(self, x, y):

        parent_x = self.collapsing_find(x)
        parent_y = self.collapsing_find(y)
        if parent_x == parent_y:
            return

        if self.sizes[parent_x] > self.sizes[parent_y]:
            self.parents[parent_y] = parent_x
            self.sizes[parent_x] += self.sizes[parent_y]
        else:
            self.parents[parent_x] = parent_y
            self.sizes[parent_y] += self.sizes[parent_x]


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        uf = UnionFind(grid)
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc

                        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                            uf.weighted_union((row, col), (nr, nc))
     
        if uf.sizes:
            return max(uf.sizes.values())
        else:
            return 0

        
      

