class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        heap = [(0, 0, 0)]
        ROWS, COLS = len(moveTime), len(moveTime[0])

        time = [[float("inf")] * COLS for _ in range(ROWS)]
        time[0][0] = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:

            curr_time, row, col = heapq.heappop(heap)

            if curr_time > time[row][col]:
                continue

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if not (0 <= nr < ROWS and 0 <= nc < COLS):
                    continue

                arrival_time = max(curr_time, moveTime[nr][nc]) + 1
                if arrival_time < time[nr][nc]:
                    time[nr][nc] = arrival_time
                    heapq.heappush(heap, (arrival_time, nr, nc))

        return time[ROWS - 1][COLS - 1]

