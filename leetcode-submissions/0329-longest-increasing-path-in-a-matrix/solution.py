class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        ROWS = len(matrix)
        COLS = len(matrix[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        memo = [[None] * COLS for _ in range(ROWS)]
        result = 0

        def dfs(max_path, row, col):

            if memo[row][col]:
                return memo[row][col]

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if not (0 <= nr < ROWS and 0 <= nc < COLS):
                    continue

                if matrix[nr][nc] <= matrix[row][col]:
                    continue

                max_path = max(max_path, 1 + dfs(1, nr, nc))

            memo[row][col] = max_path
            return max_path

        result = 0
        for row in range(ROWS):
            for col in range(COLS):
                result = max(result, dfs(1, row, col))

        return result

