class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(row: int, col: int) -> None:
            """
            DFS on the first island. Flip the 1's to 2's
            so we'll be able to identify the second island.
            """

            grid[row][col] = 2
            visited.add((row, col))

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if not (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and grid[nr][nc] == 1
                    and (nr, nc) not in visited
                ):
                    continue

                dfs(nr, nc)

        # Run dfs from the first 1's cell. DFS will mark island 1 cells.
        for r in range(ROWS):
            run = False
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)
                    run = True
                    break

            if run:
                break

        # Multi-source BFS starting from
        q = deque([(0, cell) for cell in visited])
        min_dist = float("inf")

        while q:

            dist, curr = q.popleft()
            row, col = curr

            if grid[row][col] == 1:
                min_dist = min(min_dist, dist)

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if not (0 <= nr < ROWS and 0 <= nc < COLS):
                    continue

                # Push the cell to the queue if it was not visited
                if (nr, nc) in visited:
                    continue

                visited.add((nr, nc))
                q.append((dist + 1, (nr, nc)))

        return min_dist - 1

