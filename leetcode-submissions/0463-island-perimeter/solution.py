class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        perimeter = 0
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    perimeter += 4
                    for dx, dy in directions:
                        x, y = row + dx, col + dy
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                            perimeter -= 1

        return perimeter

