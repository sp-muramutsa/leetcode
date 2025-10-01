class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        # source: (0, 0)
        # moveTime[i][j]: min time the room opens and can be moved to
        # cost = 1
        # dest = (n - 1, m - 1)
        # horizontal or vertical

        # Dijkstra

        ROWS, COLS = len(moveTime), len(moveTime[0])
        times = {(row, col): float("inf") for row in range(ROWS) for col in range(COLS)}
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        min_heap = [(0, 0)]
        times[(0, 0)] = 0

        while min_heap:

            row, col = heapq.heappop(min_heap)

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS:

                    new_time = max(times[(row, col)], moveTime[nr][nc]) + 1

                    if new_time < times[(nr, nc)]:
                        times[(nr, nc)] = new_time
                        heapq.heappush(min_heap, (nr, nc))

        return times[(ROWS - 1, COLS - 1)]

