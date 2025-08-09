class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        time = 0
        rotten = set()

        def bfs(rotten):

            changed = False

            for row, col in rotten.copy():

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if not (0 <= nr < ROWS and 0 <= nc < COLS):
                        continue

                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        rotten.add((nr, nc))
                        changed = True

            return changed

        rotten = set()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    rotten.add((row, col))

        while True:
            flag = bfs(rotten)
            if flag == False:
                break
            time += 1

        # Check if there is any fresh tomato
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return -1

        return time

