class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights), len(heights[0])
        result = []

        q = deque()
        for i in range(COLS):
            q.append((0, i))

        for j in range(ROWS):
            q.append((j, 0))

        pacific = set(q)
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:

            row, col = q.popleft()
            visited.add((row, col))

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if not (0 <= nr < ROWS and 0 <= nc < COLS):
                    continue

                if (nr, nc) in visited:
                    continue

                if heights[row][col] <= heights[nr][nc]:
                    pacific.add((nr, nc))
                    q.append((nr, nc))

        print(pacific)
        q = deque()
        for k in range(COLS):
            q.append((ROWS - 1, k))

        for l in range(ROWS):
            q.append((l, COLS - 1))

        visited = set()
        atlantic = set(q)

        while q:

            row, col = q.popleft()
            visited.add((row, col))

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if not (0 <= nr < ROWS and 0 <= nc < COLS):
                    continue

                if (nr, nc) in visited:
                    continue

                if heights[row][col] <= heights[nr][nc]:
                    atlantic.add((nr, nc))
                    q.append((nr, nc))

        print(atlantic)
        result = pacific.intersection(atlantic)
        return list(result)

