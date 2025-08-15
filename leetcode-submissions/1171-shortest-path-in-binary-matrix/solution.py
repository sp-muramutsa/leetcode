class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        # BFS

        if grid[0][0] != 0:
            return -1

        n = len(grid)
        q = deque([(1, 0, 0)])
        grid[0][0] = -1
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        while q:

            path_length, row, col = q.popleft()

            if row == n - 1 and col == n - 1:
                return path_length

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if not (0 <= nr < n and 0 <= nc < n):
                    continue

                if grid[nr][nc] == 0:
                    grid[nr][nc] = -1
                    q.append((path_length + 1, nr, nc))

        return -1

