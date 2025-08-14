from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # Keep a queue with the gates
        # While queue
        # Get the neighbors 
        # Increament the current level
        # Add them to the visited data structure
        queue = deque()
        visited = set()

        def get_neighbors(grid, position):
            new_row = [1, 0, -1, 0]
            new_col = [0, 1, 0, -1]
            moves = []
            for i in range(4):
                r = position[0] + new_row[i]
                c = position[1] + new_col[i]

                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != -1 and grid[r][c] != 0:
                    moves.append((r, c))

            return moves

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
         
        distance = 0
        while queue:
            l = len(queue)
            for _ in range(l):
                n = queue.popleft()
                rooms[n[0]][n[1]] = distance
                for p in get_neighbors(rooms, n):
                    if p in visited:
                        continue
                    visited.add((p[0], p[1]))
                    queue.append((p[0], p[1]))
            distance += 1
