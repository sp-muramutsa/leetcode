class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        time = 0
        heap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    

        while heap:

            height, row, col = heapq.heappop(heap)
            
            # Goal 
            if row == ROWS - 1 and col == COLS - 1:
                return height

            
            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if (nr, nc) in visited:
                    continue

                if not (0 <= nr < ROWS and 0 <= nc < COLS):
                    continue
                
                visited.add((nr, nc))
                heapq.heappush(heap, (max(grid[nr][nc], height), nr, nc))

        
