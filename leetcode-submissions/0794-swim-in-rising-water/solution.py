class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        heap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])


        # BFS 

        while heap:

            t, row, col = heapq.heappop(heap)

            if row == ROWS - 1 and col == COLS - 1:
                return t

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if not (0 <= nr < ROWS and 0 <= nc < COLS) or (nr, nc) in visited:
                    continue

                visited.add((nr, nc))
                new_t = max(t, grid[nr][nc])
                heapq.heappush(heap, (new_t, nr, nc))
        



                

