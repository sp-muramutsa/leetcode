class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(mat), len(mat[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        matrix = [[0] * COLS for _ in range(ROWS)]

        q = deque()
        seen = set()
        for i in range(ROWS):
            for j in range(COLS):
                if mat[i][j] == 0:
                    q.append((0, i, j))
                    seen.add((i, j))

        while q:

            path_len, row, col = q.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if not (0 <= nr < ROWS and 0 <= nc < COLS):
                    continue

                if (nr, nc) in seen:
                    continue
                
                matrix[nr][nc] = path_len + 1
                seen.add((nr, nc))
                q.append((path_len + 1, nr, nc))

        return matrix

