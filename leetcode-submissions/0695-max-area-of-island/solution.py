from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Using BFS we will iterate over each island
        # Create a get neighbor function
        # Create a result variable
        # BFS inplementation
        # Iterate through each value
        # Create a visited data structure
        # If the value is 0 skip
        # Create a queue
        # Create a temp area
        # Add the specific cell
        # While queue
        # Pop from the queue
        # Get the neighbors
        # If the neighbor is in visited we skip
        # Increament the temp value and store the cell in visited
        # Update the result with temp area
        # Return result

        def get_neighbor(cell, grid):
            new_row = [1, 0, -1, 0]
            new_col = [0, 1, 0, -1]
            moves = []

            for i in range(4):
                r = cell[0] + new_row[i]
                c = cell[1] + new_col[i]

                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
                    moves.append((r, c))
            return moves

        def bfs(grid):
            visited = set()
            res = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 0 or (i, j) in visited:
                        continue

                    queue = deque([(i, j)])
                    tmp = 1
                    visited.add((i, j))
                    while queue:
                        n = queue.popleft()
                        for neighbor in get_neighbor((n[0], n[1]), grid):
                            if (neighbor[0], neighbor[1]) in visited:
                                continue
                            visited.add((neighbor[0], neighbor[1]))
                            queue.append((neighbor[0], neighbor[1]))
                            tmp += 1

                    res = max(res, tmp)

            return res

        return bfs(grid)

