class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        patterns = set()

        def dfs_make_island(row, col):

            if (row, col) in visited or grid[row][col] == 0:
                return

            visited.add((row, col))
            curr_pattern.add((row - row_origin, col - col_origin))

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if not (0 <= nr < ROWS and 0 <= nc < COLS):
                    continue

                dfs_make_island(nr, nc)

        islands = []
        for row in range(ROWS):
            for col in range(COLS):
                curr_pattern = set()
                row_origin, col_origin = row, col
                dfs_make_island(row, col)
                if curr_pattern:
                    patterns.add(frozenset(curr_pattern))

        return len(patterns)

