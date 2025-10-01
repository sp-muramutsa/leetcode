class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        # Multi-source BFS
        # Start from the gates

        ROWS, COLS = len(rooms), len(rooms[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(source):
    
            q = deque([(source, 0)])
            visited = set()

            while q:

                curr, dist = q.popleft()
                r, c = curr
           
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < ROWS and 0 <= nc < COLS) \
                    and rooms[nr][nc] != -1 and rooms[nr][nc] != 0 and (nr, nc) not in visited:
                        rooms[nr][nc] = min(dist + 1, rooms[nr][nc])
                        q.append(((nr, nc), dist + 1))
                        visited.add((nr, nc))

        
        for row in range(ROWS):
            for col in range(COLS):
                if rooms[row][col] == 0:
                    rooms[row][col] == -2 # Mark visited
                    bfs((row, col)) # Explore neighbors

        
        
