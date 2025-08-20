from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Get all cells with rotten tomatoes
        # Add them to a queue
        # Add them to visited data structure
        # Create result minutes
        # While queue
        # Get the length pop from queue
        # Check the neighbors, if neighbors are 1 and not visited we add them to the queue and we change them to 1
        # Increameant the result
        # Return result

        def get_neighbors(cell, grid):
            new_row = [1, 0, -1, 0]
            new_column = [0, 1, 0, -1]
            moves = []

            for i in range(4):
                r = new_row[i] + cell[0]
                c = new_column[i] + cell[1]

                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
                    moves.append((r, c))

            return moves

        def get_rotten(grid):
            cell = []
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 2:
                        cell.append((i, j))

            return cell

        def is_fresh(grid):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        return True

            return False

        def bfs(grid):
            visited = set()
            queue = deque()
            cells = get_rotten(grid)
            
            for i in cells:
                queue.append(i)
                visited.add(i)

            minutes = 0
            while queue:
                l = len(queue)
                changed = False
                for _ in range(l):
                    n = queue.popleft()

                    for j in get_neighbors(n, grid):
                        if j in visited:
                            continue
                        changed = True
                        visited.add(j)
                        queue.append(j)
                        grid[j[0]][j[1]] = 2
                if changed:
                    minutes += 1

            if is_fresh(grid):
                return -1

            return minutes

        return bfs(grid)
