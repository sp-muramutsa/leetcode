class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def bfs(q):
            found = False
            new_q = deque()

            while q:

                row, col = q.popleft()

                if grid[row][col] == 1:
                    grid[row][col] = 2

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        found = True
                        new_q.append((nr, nc))

            return found, new_q

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(grid), len(grid[0])

        time = 0
        q = deque()

        # First rottens
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))

        # Start rotting
        while True:
            found, q = bfs(q)
            if not found:
                break
            
            time += 1

        # Return
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return time 

