class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        DFS
        """

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs_make_island(row, col):

            visited.add((row, col))

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if not (0 <= nr < ROWS and 0 <= nc < COLS):
                    continue

                if (nr, nc) in visited:
                    continue

                if grid[nr][nc] == "1":
                    dfs_make_island(nr, nc)

        num_islands = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs_make_island(row, col)
                    num_islands += 1

        return num_islands

